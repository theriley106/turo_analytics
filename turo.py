import requests

CENTER_LAT = 39.8283
# Center of US
CENTER_LONG = 98.5795
# Center of US

AIRPORTS_URL = "https://turo.com/api/airports?alphaCountryCode=US&includeVehicleCount=true&latitude={0}&longitude={1}&maxDistanceInMiles={2}&maxNumberOfResults={3}"

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://turo.com/api/search?airportCode=SFO&defaultZoomLevel=11&endDate=06%2F04%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&location=SFO%20%E2%80%94%20San%20Francisco%20International%20Airport%2C%20San%20Francisco%2C%20CA&locationType=Airport&maximumDistanceInMiles=30&sortType=RELEVANCE&startDate=05%2F28%2F2018&startTime=10%3A00', headers=headers, cookies=cookies)

def getMakes():
    return requests.get("https://turo.com/api/search/makes")

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
    print len(returnAirports())
