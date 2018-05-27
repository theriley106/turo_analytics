import requests
import random
import json

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
        stringVal = "&maximumPrice={}&minimumPrice={}".format(i+increments, i)
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

def searchAirport(airportCode):
    allVehicles = []
    for prices in genMinMax():
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

if __name__ == '__main__':
    #e = (minRequest(RESULTS_URL.format(genDates())).json())
    #print json.dumps(e)
    print len(searchAirport("SFO"))
    #print len(returnAirports())
