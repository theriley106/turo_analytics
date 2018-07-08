import threading
import grabAll
import os
import json
global COUNT
COUNT = 0
THREADS=20
lock = threading.Lock()
lngLatList = []
for val in open("listOfLongLat.txt").read().split("\n"):
	info = {"lng": val.split(",")[0].strip(), 'lat': val.split(",")[1]}
	lngLatList.append(info)

def append_record(record):
	lock.acquire()
	with open('my_file.json', 'a') as f:
		json.dump(record, f)
		f.write(os.linesep)
	lock.release()

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]

listOfURLs = chunks(lngLatList, int(len(lngLatList)/THREADS))

def searchVal(dictVal):
	global COUNT
	for dictVal in dictVal:
		try:
			print("Grabbing: {} {} | Car # {}".format(dictVal['lat'], dictVal['lng'], COUNT))
			a = grabAll.grabCars(dictVal['lat'], dictVal['lng'])
			for e in a:
				COUNT = COUNT + 1
				append_record(e)
		except Exception as exp:
			print exp

threads = [threading.Thread(target=searchVal, args=(ar,)) for ar in listOfURLs]
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
