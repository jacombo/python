#!/usr/bin/python3

import requests
from pprint import pprint
import operator

response = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.json')

print("***************************************************************")
print("Aktualizovano:%s\nZdroj:%s" % (response.json()['modified'],response.json()['source']))
print("***************************************************************")

summary = {}
age_count = 0
total_deaths = 0
for item in response.json()['data']:
    #print("%s %s" % (item['vek'], round(item['vek'],-1)))
    age = round(item['vek'],-1)
    age_count = age_count + age

    if age in summary:
        count = summary[age]
    else:
        count = 1    
    
    summary[age] = count + 1
    total_deaths = total_deaths + 1

# Sort Dictionary by value using itemgetter
sorted_dict = dict(sorted(summary.items(),
                            key=operator.itemgetter(1),
                            reverse=True))

for k,v in sorted_dict.items():
    print("Vek:%s+\t\tpocet umrti:%s\t\t%s%%" % (k,v, round((v / total_deaths) * 100, 1)))

print("\nPrumerny vek mrtvych:%s" % (round(age_count / total_deaths, 1)))
print("\nCelkovy pocet mrtvych:%s" % (total_deaths))
print("***************************************************************")
