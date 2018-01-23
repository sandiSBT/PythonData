import json 
import urllib2

url="https://data.sfgov.org/api/views/yitu-d5am/rows.json"
data = json.load(urllib2.urlopen(url))
print data["meta"]["view"]["columns"][14]['name']

statesurl = "http://baselayertraining.herokuapp.com/api/states"
# Load the data
# Log the keys for the midwest states
# Log the values for the midwest states
# Log the value for California
data = json.load(urllib2.urlopen(statesurl))
print data["midwest"].keys()
print data["midwest"].values()
print data["west"]["CA"]

































