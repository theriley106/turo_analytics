from uszipcode import ZipcodeSearchEngine
from math import radians, cos, sin, asin, sqrt
import math
import os

search = ZipcodeSearchEngine()

res = search.by_coordinate(39.122229, -77.133578, radius=30000, returns=5000000)
# This returns every us zip code

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def findpoints(lon, lat):
    radius = 10
    N = 360

    # generate points
    circlePoints = []
    for k in range(N):
        angle = math.pi*2*k/N
        dx = radius*math.cos(angle)
        dy = radius*math.sin(angle)
        point = {}
        point['lat']= lat + (180/math.pi)*(dy/6371) #Earth Radius
        point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        # add to list
        circlePoints.append(point)
    return circlePoints


if __name__ == '__main__':
	#if radius is not in the
	radius = int(raw_input("Input Radius: "))
	'''	for f in res:
		for val in res:
			if
	for val in res:
		raw_input(len(findpoints(val.Longitude, val.Latitude)))'''
	print len(res)
	listOfPoints = []
	for r, tmpVal in enumerate(res):
		save = True
		for val in listOfPoints:
			if haversine(tmpVal.Longitude, tmpVal.Latitude, val.Longitude, val.Latitude) > (radius):
				pass
			else:
				save = False
				break
		if save == True:
			listOfPoints.append(tmpVal)
		print("{}/{}".format(r, len(res)))

	print("{} Lng/Lat coverign a {} Mile Radius".format(len(listOfPoints), radius))
	lngLatList = []
	for val in listOfPoints:
		stringVal = "{},{}".format(val.Longitude, val.Latitude)
		lngLatList.append(stringVal)
	file = open("listOfLongLat.txt", "w")
	file.write("\n".join(lngLatList))
	os.system("cp listOfLongLat.txt ../../GraphicalChallenge/static/listOfLongLat.txt")
	#longestDistance =

'''
# http://en.wikipedia.org/wiki/Extreme_points_of_the_United_States#Westernmost
top = 49.3457868 # north lat
left = -124.7844079 # west long
right = -66.9513812 # east long
bottom =  24.7433195 # south lat

def cull(l):
    c = []
    for (lat, lng) in l:
        if bottom <= lat <= top and left <= lng <= right:
            c.append((lat, lng))
'''
