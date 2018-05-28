import requests
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


if __name__ == '__main__':
	a = modelX()
	print len(a)
