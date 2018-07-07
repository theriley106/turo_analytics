import requests
import random
import json
import glob

CENTER_LAT = 39.8283
# Center of US
CENTER_LONG = 98.5795
# Center of US
THIS_MONTH = 5
# This is the numerical value of this month | ie May

AIRPORTS_URL = "https://turo.com/api/airports?alphaCountryCode=US&includeVehicleCount=true&latitude={0}&longitude={1}&maxDistanceInMiles={2}&maxNumberOfResults={3}"
RESULTS_URL = "https://turo.com/api/search?airportCode={0}&country=US&itemsPerPage=200&maxNumberOfResults=200&locationType=Airport&maximumDistanceInMiles=60{1}"
FUTURE_TIME = 2
# Months in advance - to make sure you're not searching already matched vehicles


def getMakes():
	return requests.get("https://turo.com/api/search/makes")

#def genData():

def genMinMax(increments=50):
	# Returns list of strings
	listOfStrings = []
	for i in range(0, 250, increments):
		maxPrice = i+increments
		if maxPrice > 250:
			maxPrice = 250
		stringVal = "&maximumPrice={}&minimumPrice={}".format(maxPrice, i)
		listOfStrings.append(stringVal)
	return listOfStrings


def genDates(timeFrame=1):
	# Timeframe is the total rental time
	# Returns a string
	randomMonth = random.randint(THIS_MONTH+FUTURE_TIME, 9)
	randomDay = random.randint(1, 9)
	randomTime = random.randint(1, 9)
	startDate = "&startDate=0{}%2F{}%2F2018".format(randomMonth, randomDay)
	startTime = "&startTime=0{}%3A00".format(randomTime)
	endDate = "&endDate=0{}%2F{}%2F2018".format(randomMonth, randomDay+timeFrame)
	endTime = "&endTime=0{}%3A00".format(randomTime)
	return startDate + startTime + endDate + endTime

def searchAirport(airportCode, increments=50):
	allVehicles = []
	for prices in genMinMax(increments):
		url = RESULTS_URL.format(airportCode, genDates())
		url += prices
		a = minRequest(url).json()
		for val in a['list']:
			allVehicles.append(val)
	return allVehicles

def minRequest(url):
	headers = {'Referer': 'https://turo.com/search?country=US&'}
	return requests.get(url, headers=headers)

def returnAirports(latitude=None, longitude=None, maxDistance=7000, maxResults=500):
	# Returns airports | Inputting no parameters will return all airports
	if latitude == None or longitude == None:
		# This means the info wasn't inputted
		latitude = CENTER_LAT
		longitude = CENTER_LONG
	url = AIRPORTS_URL.format(latitude, longitude, maxDistance, maxResults)
	# Creates the URL
	return minRequest(url).json()

def genAllURLS():
	returnAirports()

def getMoreInfo(vehicleURL):
	vehicleID = vehicleURL[::-1].partition("/")[0][::-1]
	params = (
	    ('vehicleId', vehicleID),
	    )
	response = requests.get('https://turo.com/api/vehicle/detail', headers={'Referer': 'https://turo.com{}'.format(vehicleURL)}, params=params, cookies={})
	return response

class search(object):
	def __init__(self):
		self.database = []
		for file in glob.glob('./database/moreInfo*.json'):
			for car in json.load(open(file)):
				self.database.append(car)

	def keyword(self, keyword):
		allResults = []
		for val in self.database:
			if str(keyword).lower() in str(val).lower():
				allResults.append(val)
		return allResults

	def priceFromKeyword(self, keywordVal):
		allPrices = []
		for val in self.keyword(keywordVal):
			allPrices.append(val['rate']['averageDailyPrice'])
		try:
			average = float(sum(allPrices)) / float(len(allPrices))
		except:
			average = 0
		return average

	def searchByMake(self, make):
		allResults = []
		for val in self.database:
			try:
				if val['vehicle']['make'].lower() == make.lower():
					allResults.append(val)
			except:
				pass
		return allResults

	def searchByModel(self, model):
		allResults = []
		for val in self.database:
			try:
				if val['vehicle']['model'].lower() == model.lower():
					allResults.append(val)
			except:
				pass
		return allResults

	def searchByModelYear(self, model, year):
		allResults = []
		for val in self.database:
			try:
				if val['vehicle']['model'].lower() == model.lower() and val['vehicle']['year'] == year:
					allResults.append(val)
			except:
				pass
		return allResults

	#def search(self, model=None, make=None, year=None, )



if __name__ == '__main__':
	with open('airports.json', 'w') as outfile:
		json.dump(returnAirports(), outfile)
	'''for val in a.keyword('bugatti'):
		model = val['vehicle']['model']
		trim = val['vehicle']['trim']
		if trim != None:
			model += " {}".format(trim)
		city = val['location']['city']
		dailyPrice = val['rate']['averageDailyPrice']
		print("${} {} in {}".format(dailyPrice, model, city))'''
