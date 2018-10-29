import csv


with open('Economics.csv', 'rb') as f:
	reader = csv.reader(f)
	ALL_DATA = list(reader)

DB = {}
PRICE_ONLY = [float(e[1].replace(",", "")) for e in ALL_DATA]
AVERAGE = float(sum(PRICE_ONLY)) / float(len(PRICE_ONLY))

for val in ALL_DATA:
	DB[val[0]] = float(val[1].replace(",", "")) / AVERAGE


def Status(zipVal):
	try:
		return round(DB[str(zipVal)], 2)
	except:
		return 0


if __name__ == '__main__':
	print Status(94030)
