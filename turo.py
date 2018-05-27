import requests

cookies = {
    'rr_u_cid': 'AM4Pn2OnRkaQHLm8s43yDA',
    'JSESSIONID': 'a52c949c-a1be-4902-9f23-5f88caf62227',
    'ajs_anonymous_id': '%222cc4aaee-2fbd-4b77-a7cb-ed87c50ff23b%22',
    'ajs_user_id': 'null',
    'ajs_group_id': 'null',
    'preferredLocale': 'en_US',
    'sid': 'mZCfmDHyTAWMku-p9mPhZw',
    'times': '{%22startDate%22:%2205/28/2018%22%2C%22startTime%22:%2210:00%22%2C%22endDate%22:%2206/04/2018%22%2C%22endTime%22:%2210:00%22}',
    'airportCode': 'SFO',
}

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://turo.com/search?airportCode=SFO&defaultZoomLevel=11&endDate=06%2F04%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&location=SFO%20%E2%80%94%20San%20Francisco%20International%20Airport%2C%20San%20Francisco%2C%20CA&locationType=Airport&maximumDistanceInMiles=30&sortType=RELEVANCE&startDate=05%2F28%2F2018&startTime=10%3A00',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}

params = (
    ('airportCode', 'SFO'),
    ('endDate', '06/04/2018'),
    ('endTime', '10:00'),
    ('isMapSearch', 'false'),
    ('itemsPerPage', '1000'),
    ('sortType', 'RELEVANCE'),
    ('startDate', '05/28/2018'),
    ('startTime', '10:00'),
)

response = requests.get('https://turo.com/api/search', headers=headers, params=params, cookies=cookies)
print len(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://turo.com/api/search?airportCode=SFO&defaultZoomLevel=11&endDate=06%2F04%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&location=SFO%20%E2%80%94%20San%20Francisco%20International%20Airport%2C%20San%20Francisco%2C%20CA&locationType=Airport&maximumDistanceInMiles=30&sortType=RELEVANCE&startDate=05%2F28%2F2018&startTime=10%3A00', headers=headers, cookies=cookies)

def getMakes():
    return requests.get("https://turo.com/api/search/makes")

def minRequest(url):
    headers = {'Referer': 'https://turo.com/search?country=US&'}
    return requests.get(url, header=headers)
