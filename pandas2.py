# sudo pip install pandas
# password: post

import pandas as pd
import numpy as np


vacation = pd.Series([350, 500, 50, 10],
					  index=['flight',
					  		 'hotel',
					  		 'dinner',
					  		 'ice cream'])


print(vacation.sum())

mysample = pd.DataFrame([
	[1,3],[4,5],
	[1,3],[4,5],
	[1,3],[4,5]
])

print(mysample)
print(mysample.sum()) # sum colms
print(mysample.sum(axis=1)) # sum rows


print("-" * 20)
#Getting Unique
mydata = pd.Series(['c','c','c','a','a','b'])
mydata_uniques = mydata.unique()
print(mydata_uniques)

#filling in blank
vacation2 = pd.Series([np.nan, 500, np.nan, 10],
					  index=['flight',
					  		 'hotel',
					  		 'dinner',
					  		 'ice cream'])

print("-" * 20)
print(vacation2)

vacation3 = vacation2.fillna(0)
print(vacation3)
