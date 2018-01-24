# load json from internet into pandas DataFrame

from urllib.request import urlopen # used to connect to internet json
import json
from pandas.io.json import json_normalize # used to convert json directly to DataFrame
import pandas as pd

response = urlopen("https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-ETC")
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = json_normalize(d['result'])
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df = df.set_index('TimeStamp')

print (df.head())
