import json
f = open('PSExample.json')
data = json.load(f)
data2 = data['data']
print(type(data2))
data3 = data2[0]
print(type(data3))
lat = data3['latitude']
long = data3['longitude']
print(lat)
print(long)