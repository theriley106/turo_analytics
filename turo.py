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
RESULTS_URL = "https://turo.com/api/search?airportCode=SFO&country=US&defaultZoomLevel=7&international=true&isMapSearch=false&itemsPerPage=500&maxNumberOfResults=500&locationType=Airport&maximumDistanceInMiles=60&region=CA&sortType=RELEVANCE{0}"



def getMakes():
    return requests.get("https://turo.com/api/search/makes")

#def genData():

def genMinMax(increments=50):
    # Returns list of strings
    listOfStrings = []
    for i in range(0, 250, increments):
        stringVal = "&maximumPrice={}&minimumPrice={}".format(i, i+increments)
        listOfStrings.append(stringVal)
    return listOfStrings


def genDates(timeFrame=1):
    # Timeframe is the total rental time
    # Returns a string
    randomMonth = random.randint(THIS_MONTH+1, 12)
    randomDay = random.randint(1, 28)
    randomTime = random.randint(1, 9)
    startDate = "&startDate=0{}%2F{}%2F2018".format(randomMonth, randomDay)
    startTime = "&startTime=0{}%3A00".format(randomTime)
    endDate = "&endDate=0{}%2F{}%2F2018".format(randomMonth, randomDay+timeFrame)
    endTime = "&endTime=0{}%3A00".format(randomTime)
    return startDate + startTime + endDate + endTime

#def searchAirport():


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

if __name__ == '__main__':
    e = (minRequest(RESULTS_URL.format(genDates())).json())
    print json.dumps(e)
    #print len(returnAirports())
