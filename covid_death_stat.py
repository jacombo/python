#!/usr/bin/python3

import requests
from pprint import pprint
import operator

response = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.json')

print("*****************************************************************************")
print("Datum:%s\tzdroj:%s" % (response.json()['modified'],response.json()['source']))
print("*****************************************************************************")

sum = {}
age_count = 0
for item in response.json()['data']:
    #print("%s %s" % (item['vek'], round(item['vek'],-1)))
    age = round(item['vek'],-1)
    age_count = age_count + age

    if age in sum:
        count = sum[age]
    else:
        count = 1    
    
    sum[age] = count + 1

# Sort Dictionary by value using itemgetter
sorted_dict = dict(sorted(sum.items(),
                            key=operator.itemgetter(1),
                            reverse=True))
total = 0
for k,v in sorted_dict.items():
    print("Vek:%s\tpocet umrti:%s" % (k,v))
    total = total + v

print("\nPrumerny vek mrtvych:%s" % (age_count / total))
print("\nCelkovy pocet mrtvych:%s" % (total))
print("*****************************************************************************")

