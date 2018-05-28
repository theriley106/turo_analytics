import requests

vehicleURL = "/rentals/suvs/ma/boston/tesla-model-x/284418"
vehicleID = vehicleURL[::-1].partition("/")[0][::-1]
params = (
    ('vehicleId', vehicleID),
    )
response = requests.get('https://turo.com/api/vehicle/detail', headers={'Referer': 'https://turo.com{}'.format(vehicleURL)}, params=params, cookies={})

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://turo.com/api/vehicle/detail?endDate=06%2F04%2F2018&endTime=10%3A00&startDate=05%2F28%2F2018&startTime=10%3A00&vehicleId=284418', headers=headers, cookies=cookies)
e = response.json()['vehicle']
print ['trim']
