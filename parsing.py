# show data first
# trying to connect and show the name of the 14th column

import urllib3
import json

http = urllib3.PoolManager()
url="http://data.sfgov.org/api/views/yitu-d5am/rows.json"
r = http.request('GET', url)
stuff = json.loads(r.data.decode('utf-8'))

print(stuff["meta"]["view"]["columns"][14]['name'])
'''
statesurl = "http://baselayertraining.herokuapp.com/api/states"
# Load the data
# Log the keys for the midwest states
# Log the values for the midwest states
# Log the value for California

data = json.load(urllib3.urlopen(statesurl))
print(data["midwest"].keys())
print(data["midwest"].values())
print(data["west"]["CA"])

'''































