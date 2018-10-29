import requests
import re
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class search(object):
	def __init__(self):
		pass


def modelS():
	allVehicles = []
	count = requests.get("https://www.truecar.com/abp/api/vehicles/search/vehicles?fallback=true&make_slug=tesla&model_slug=model-s&page=1", headers=headers).json()['count']
	e = 1
	for i in range(0, count, 30):
		res = requests.get("https://www.truecar.com/abp/api/vehicles/search/vehicles?fallback=true&make_slug=tesla&model_slug=model-s&page={}".format(e), headers=headers)
		for val in res.json()['vehicles']:
			allVehicles.append(val)
		e += 1
	return allVehicles

def modelX():
	allVehicles = []
	count = requests.get("https://www.truecar.com/abp/api/vehicles/search/vehicles?fallback=true&make_slug=tesla&model_slug=model-x&page=1", headers=headers).json()['count']
	e = 1
	for i in range(0, count, 30):
		res = requests.get("https://www.truecar.com/abp/api/vehicles/search/vehicles?fallback=true&make_slug=tesla&model_slug=model-x&page={}".format(e), headers=headers)
		for val in res.json()['vehicles']:
			allVehicles.append(val)
		e += 1
	return allVehicles

'''
Script to grab Model S Pricing:

trims = {}
	trimList = []
	a = modelS()
	for val in a:
		trimList.append(val['trim'])
	for trim in list(set(trimList)):
		if trim not in trims:
			trims[trim] = []
		for val in a:
			if val['trim'] == trim:
				trims[trim].append(val['list_price'])
		trims[trim] = float("{0:.2f}".format((float(sum(trims[trim])) / float(len(trims[trim])))))
	with open('modelSPricing.json', 'w') as outfile:
		json.dump(trims, outfile)

'''


if __name__ == '__main__':
	trims = {}
	trimList = []
	a = modelX()
	for val in a:
		trimList.append(val['trim'])
	for trim in list(set(trimList)):
		if trim not in trims:
			trims[trim] = []
		for val in a:
			if val['trim'] == trim:
				trims[trim].append(val['list_price'])
		trims[trim] = float("{0:.2f}".format((float(sum(trims[trim])) / float(len(trims[trim])))))
	with open('modelXPricing.json', 'w') as outfile:
		json.dump(trims, outfile)


