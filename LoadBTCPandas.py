# another way to load json data from internet. 
# Not as reliable
# missing columns in output

import pandas as pd

df = pd.read_json('https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-ETC')
df = pd.DataFrame(df['result'].values.tolist())
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df = df.set_index('TimeStamp')
print (df.head())