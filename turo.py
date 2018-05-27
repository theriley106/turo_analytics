import requests

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://turo.com/api/search?airportCode=SFO&defaultZoomLevel=11&endDate=06%2F04%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&location=SFO%20%E2%80%94%20San%20Francisco%20International%20Airport%2C%20San%20Francisco%2C%20CA&locationType=Airport&maximumDistanceInMiles=30&sortType=RELEVANCE&startDate=05%2F28%2F2018&startTime=10%3A00', headers=headers, cookies=cookies)

def getMakes():
    return requests.get("https://turo.com/api/search/makes")

def minRequest(url):
    headers = {'Referer': 'https://turo.com/search?country=US&'}
    return requests.get(url, headers=headers)

if __name__ == '__main__':
    print minRequest('https://turo.com/api/airports?alphaCountryCode=US&excludeLowActivityAirports=true&includeVehicleCount=true&latitude=33.22344050092164&longitude=-87.6465401142578&maxDistanceInMiles=100&maxNumberOfResults=500').json()
