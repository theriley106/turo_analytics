import requests

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://turo.com/search?',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}

params = (
    ('country', 'US'),
    ('defaultZoomLevel', '14'),
    ('endDate', '07/15/2018'),
    ('endTime', '10:00'),
    ('international', 'true'),
    ('isMapSearch', 'true'),
    ('itemsPerPage', '200'),
    ('location', 'Map location'),
    ('locationType', 'place'),
    ('maximumDistanceInMiles', '10'),
    ('Latitude', '39.1329803'),
    ('Longitude', '-77.1370115'),
    ('sortType', 'RELEVANCE'),
    ('startDate', '07/08/2018'),
    ('startTime', '10:00'),
)

response = requests.get('https://turo.com/api/search', headers=headers, params=params)
print response.json()['list']
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://turo.com/api/search?country=US&defaultZoomLevel=14&endDate=07%2F15%2F2018&endTime=10%3A00&international=true&isMapSearch=true&itemsPerPage=200&location=Map%20location&locationType=place&maximumDistanceInMiles=10&northEastLatitude=32.985443258413&northEastLongitude=-96.77522385150145&region=TX&sortType=RELEVANCE&southWestLatitude=32.93164620738854&southWestLongitude=-96.85015404254149&startDate=07%2F08%2F2018&startTime=10%3A00', headers=headers, cookies=cookies)
