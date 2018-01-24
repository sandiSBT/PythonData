#import numpy as np
import pandas as pd


# load all csv files into one dateframe
years = range(1880,2016)

pieces = [ ]
columns = ['name','sex','births']

for year in years:
	path = 'names/yob%d.txt' % year
	frame = pd.read_csv(path, names=columns)

	frame['year'] = year
	pieces.append(frame)

	names = pd.concat(pieces, ignore_index = True)

#print names

# how many births for each year
total_births = pd.pivot_table(names, values='births', index='year', columns='sex', aggfunc=sum)

# print(total_births)

# add prop col. fraction of babies given each name relative to birth total
def add_prop(group):
	#Integer division floors
	births = group.births.astype(float)
	group['prop'] = births / births.sum()
	return group

names = names.groupby(['year','sex']).apply(add_prop)

# print(names)


print(names.tail(1200))

# double check prop col adds to 1 NOT WORKING
# np.allclose(names.groupby(['year','sex'])['prop'].sum(),1)

