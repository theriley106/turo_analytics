import json




a = open("my_file.json").read().split("\n")
a.remove(a[-1])
print len(a)
listOfJson = []
for val in a:
	listOfJson.append(json.loads(val))

idList = []
for val in listOfJson:
	if val['vehicle']['id'] not in idList:
		idList.append(val['vehicle']['id'])
	else:
		listOfJson.remove(val)

print(len(listOfJson))
with open("newDB.json", "w") as outfile:
	json.dump(listOfJson, outfile)
