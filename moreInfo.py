import turo
import threading
import json
import random
import time
import requests
global infoList

THREADS = 20

lock = threading.Lock()

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]

def getMoreInfo(vehicleURL):
	global infoList
	for vehicleURL in vehicleURL:
		try:
			vehicleID = vehicleURL[::-1].partition("/")[0][::-1]
			params = (
			    ('vehicleId', vehicleID),
			    )
			response = requests.get('https://turo.com/api/vehicle/detail', headers={'Referer': 'https://turo.com{}'.format(vehicleURL)}, params=params, cookies={}, timeout=15)
			infoList.append(response.json())
			if len(infoList) % 50 == 0:
				print (len(infoList))
			lock.acquire()
			if len(infoList) > 1000:
				e = 'moreInfo{}.json'.format(random.randint(1,50))
				with open(e, 'w') as outfile:
					json.dump(infoList, outfile)
				print("Saved to {}".format(e))
				infoList = []
			lock.release()
		except Exception as exp:
			print exp

if __name__ == '__main__':
	infoList = []
	a = turo.search()

	listOfURLs = []
	for listing in a.database:
		listOfURLs.append(listing['vehicle']['url'])
	listOfURLs = chunks(listOfURLs, int(len(listOfURLs)/THREADS))
	threads = [threading.Thread(target=getMoreInfo, args=(ar,)) for ar in listOfURLs]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	e = 'moreInfo{}.json'.format(random.randint(1,50))
	with open(e, 'w') as outfile:
		json.dump(infoList, outfile)
	print("Saved to {}".format(e))

