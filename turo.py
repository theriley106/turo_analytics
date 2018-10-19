import requests
import random
import json
import zipfile
import glob
import os
import csv
import psycopg2
import json
import credentials
import re
ALL_KEYS = ['rating', 'owner_image_thumbnails_225x225', 'location_precision_accuracy', 'vehicle_name', 'location_timeZone', 'rate_monthly', 'distanceLabel', 'vehicle_marketCountry', 'rate_averageDailyPrice', 'vehicle_listingCreatedTime', 'vehicle_marketCurrency_decimalPlaces', 'owner_image_id', 'vehicle_marketCurrency_currencyCode', 'images_0_thumbnails_170x125', 'images_0_id', 'rate_averageDailyPriceWithCurrency_currencyCode', 'images_0_thumbnails_574x343', 'owner_lastName', 'rate_averageDailyPriceWithCurrency_amount', 'vehicle_image_verified', 'location_city', 'vehicle_id', 'location_country', 'vehicle_image_thumbnails_50x30', 'location_precision_level', 'owner_image_thumbnails_84x84', 'location_longitude', 'owner_image_placeholder', 'vehicle_make', 'images_0_verified', 'images_0_originalImageUrl', 'images_0_thumbnails_50x30', 'owner_image_thumbnails_32x32', 'vehicle_url', 'rentableFromSearchedAirport', 'vehicle_marketCurrency_defaultFractionDigits', 'responseRate', 'vehicle_image_placeholder', 'owner_image_originalImageUrl', 'rate_daily', 'deliveryLabel', 'vehicle_year', 'vehicle_image_originalImageUrl', 'reviewCount', 'owner_name', 'renterTripsTaken', 'location_addressLines_0', 'vehicle_image_resizableUrlTemplate', 'images_0_thumbnails_100x60', 'location_locationSource', 'rate_weekly', 'owner_id', 'location_address', 'images_0_resizableUrlTemplate', 'vehicle_registration', 'vehicle_image_thumbnails_170x125', 'responseTime', 'businessClass', 'vehicle_marketCurrency_symbol', 'distanceWithUnit_unit', 'vehicle_type', 'owner_image_verified', 'vehicle_image_thumbnails_620x372', 'newListing', 'distance', 'images_0_thumbnails_620x372', 'owner_image_resizableUrlTemplate', 'distanceWithUnit_scalar', 'location_state', 'vehicle_trim', 'images_0_thumbnails_170x102', 'vehicle_automaticTransmission', 'vehicle_image_thumbnails_100x60', 'distanceWithUnit_unlimited', 'freeDeliveryPromotion', 'vehicle_image_thumbnails_574x343', 'vehicle_image_id', 'owner_image_thumbnails_300x300', 'location_latitude', 'owner_firstName', 'vehicle_image_thumbnails_170x102', 'instantBookDisplayed', 'vehicle_model', 'images_0_placeholder']
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

def first_time_setup(folder_name='dataset'):
	for file in glob.glob("{}/*.zip".format(folder_name)):
		print("Extracting {}...".format(file))
		zip_ref = zipfile.ZipFile(file, 'r')
		zip_ref.extractall("{}/".format(folder_name))
		zip_ref.close()
		#print("Removing {}...".format(file))
		#os.remove(file)

def saveToCSV(listVal, saveAs):
	with open(saveAs, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(listVal)

def saveToJSON(listVal, saveAs):
	with open(saveAs, 'w') as outfile:
		json.dump(listVal, outfile)

def saveData(listVal, saveAs):
	fileExtension = saveAs[::-1].partition(".")[0][::-1]
	if fileExtension.lower() == "json":
		saveToJSON(listVal, saveAs)
	elif fileExtension.lower() == "csv":
		saveToCSV(listVal, saveAs)
	else:
		raise Exception("File type not valid...")

class search(object):
	def __init__(self):
		self.database = []

	def keyword(self, keyword):
		allResults = []
		for val in self.database:
			if str(keyword).lower() in str(val).lower():
				allResults.append(val)
		return allResults

	def getAveragePriceModel(self, vehicle_model):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		#cursor.execute("SELECT vehicle_name, rate_daily, location_address, vehicle_image_thumbnails_620x372, vehicle_year FROM turodb WHERE vehicle_id = {}".format(int(vehicle_id)))
		cursor.execute("SELECT AVG(rate_daily) FROM turodb WHERE UPPER(vehicle_model) like '{}'".format(vehicle_model.upper()))
		val = cursor.fetchone()[0]
		return round(val, 2)

	def getTotalModel(self, vehicle_model):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		#cursor.execute("SELECT vehicle_name, rate_daily, location_address, vehicle_image_thumbnails_620x372, vehicle_year FROM turodb WHERE vehicle_id = {}".format(int(vehicle_id)))
		cursor.execute("SELECT COUNT(rate_daily) FROM turodb WHERE UPPER(vehicle_model) like '{}'".format(vehicle_model.upper()))
		val = cursor.fetchone()[0]
		return int(val)

	def searchVehicleID(self, vehicle_id):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		cursor.execute("SELECT (location_longitude, location_latitude, vehicle_id, vehicle_name, vehicle_model) FROM turodb WHERE vehicle_id = {}".format(int(vehicle_id)))
		for val in cursor.fetchall():
			all_vals = [x.strip() for x in str(val[0]).split(",")]
			vehicle_model = all_vals.pop(-1).replace(")", "")
			vehicle_name = all_vals.pop(-1).replace(")", "")
			vehicle_id = all_vals.pop(-1).replace(")", "")

			val = ", ".join(all_vals)
			print val
			a, b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str(val))
		  	allResults.append([b, a, vehicle_id, vehicle_name, vehicle_model])
		conn.commit()
		cursor.close()
		return allResults


	def searchSingleID(self, vehicle_id):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		#cursor.execute("SELECT vehicle_name, rate_daily, location_address, vehicle_image_thumbnails_620x372, vehicle_year FROM turodb WHERE vehicle_id = {}".format(int(vehicle_id)))
		cursor.execute("SELECT {} FROM turodb WHERE vehicle_id = {}".format(', '.join(ALL_KEYS), int(vehicle_id)))
		for val in cursor.fetchall():
		  	allResults.append(val)
		conn.commit()
		cursor.close()
		return allResults

	def searchUserID(self, user_id):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		cursor.execute("SELECT (location_longitude, location_latitude, vehicle_id, vehicle_name, vehicle_model) FROM turodb WHERE owner_id = {}".format(int(user_id)))
		for val in cursor.fetchall():
			all_vals = [x.strip() for x in str(val[0]).split(",")]
			vehicle_model = all_vals.pop(-1).replace(")", "")
			vehicle_name = all_vals.pop(-1).replace(")", "")
			vehicle_id = all_vals.pop(-1).replace(")", "")

			val = ", ".join(all_vals)
			print val
			a, b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str(val))
		  	allResults.append([b, a, vehicle_id, vehicle_name, vehicle_model])
		conn.commit()
		cursor.close()
		return allResults

	def searchByMake(self, make, save=None):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		cursor.execute("SELECT (location_longitude, location_latitude, vehicle_id, vehicle_name, vehicle_model) FROM turodb WHERE vehicle_make = '{}'".format(make.title()))
		for val in cursor.fetchall():
			all_vals = [x.strip() for x in str(val[0]).split(",")]
			vehicle_model = all_vals.pop(-1).replace(")", "").replace('"', '')
			vehicle_name = all_vals.pop(-1).replace(")", "").replace('"', '')
			vehicle_id = all_vals.pop(-1).replace(")", "")

			val = ", ".join(all_vals)
			print val
			try:
				a, b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str(val))
			  	allResults.append([b, a, vehicle_id, vehicle_name, vehicle_model])
			except:
				pass
		conn.commit()
		cursor.close()
		return allResults

	def get_all_lng_lat(self):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		cursor.execute("SELECT (location_longitude, location_latitude, vehicle_id, vehicle_name, vehicle_model) FROM turodb")
		for val in cursor.fetchall():
			all_vals = [x.strip() for x in str(val[0]).split(",")]
			vehicle_model = all_vals.pop(-1).replace(")", "")
			vehicle_name = all_vals.pop(-1).replace(")", "")
			vehicle_id = all_vals.pop(-1).replace(")", "")

			val = ", ".join(all_vals)
			print val
			a, b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str(val))
		  	allResults.append([b, a, vehicle_id, vehicle_name, vehicle_model])
		conn.commit()
		cursor.close()
		return allResults

	def searchByModel(self, model, save=None):
		allResults = []
		conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
		cursor = conn.cursor()
		cursor.execute("SELECT (location_longitude, location_latitude, vehicle_id, vehicle_name, vehicle_model) FROM turodb WHERE vehicle_make = '{}'".format(model.title()))
		for val in cursor.fetchall():
			all_vals = [x.strip() for x in str(val[0]).split(",")]
			vehicle_model = all_vals.pop(-1).replace(")", "")
			vehicle_name = all_vals.pop(-1).replace(")", "")
			vehicle_id = all_vals.pop(-1).replace(")", "")

			val = ", ".join(all_vals)
			print val
			a, b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str(val))
		  	allResults.append([b, a, vehicle_id, vehicle_name, vehicle_model])
		conn.commit()
		cursor.close()
		return allResults


	def searchByModelYear(self, model, year, save=None):
		allResults = []
		for val in self.database:
			try:
				if val['vehicle']['model'].lower() == model.lower() and val['vehicle']['year'] == year:
					allResults.append(val)
			except:
				pass
		if save != None:
			saveData(allResults, save)
		return allResults

	#def search(self, model=None, make=None, year=None, )



if __name__ == '__main__':
	info = {}
	allResults = []
	new_vals = []
	conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
	cursor = conn.cursor()
	cursor.execute("SELECT DISTINCT vehicle_make FROM turodb")
	for val in cursor.fetchall():
		allResults.append(val[0])
	for val in allResults:
		cursor.execute("SELECT AVG(rate_daily), COUNT(rate_daily) FROM turodb WHERE vehicle_make = '{}'".format(val))
		for v in cursor.fetchall():
			a, b = v
			new_vals.append({"model": val, "count": b, "average": round(a, 2)})
	print json.dumps(new_vals)
	pass

	'''with open('airports.json', 'w') as outfile:
		json.dump(returnAirports(), outfile)'''
	'''for val in a.keyword('bugatti'):
		model = val['vehicle']['model']
		trim = val['vehicle']['trim']
		if trim != None:
			model += " {}".format(trim)
		city = val['location']['city']
		dailyPrice = val['rate']['averageDailyPrice']
		print("${} {} in {}".format(dailyPrice, model, city))'''
