import requests
import json

url = "https://dailyprayer.abdulrcs.repl.co/api/singapore"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])
print(data['today'])
# for prayer in data["today"]:
#     print(prayer + ": " + data["today"][prayer])

for x in data['today']:
    if x in 'Fajr':
        x.replace('Fajr', 'bomdod')
        print(x)
    # print(x + ' ' + data['today'][x])