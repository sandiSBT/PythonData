# sudo pip install pandas
# password: post

# Series = 1 dim array-like. contains array of data and 
# array of data labels (index)

import pandas as pd
ps = pd.Series([0, 1, 4, 9, 16, 25], name='squares')
print(ps)
print(ps.values)
print(ps.index)

# you can specify your own index
print ("-" * 10)
vacation = pd.Series([350, 500, 50, 10],
					  index=['flight', 
					  		 'hotel', 
					  		 'dinner', 
					  		 'ice cream'])
print(vacation)
print(vacation.index)
print(vacation[1])
print(vacation[2])
print(vacation['ice cream'])
print(vacation[vacation > 100])

# multiply series
print("-" * 10)
series1 = pd.Series([1, 40, 15, 30])
series2 = pd.Series([3, 1, 22, 44])
series3 = series1 * series2
print(series3)

# string series so concat					  		 
series1 = pd.Series(["one", "two"])
series2 = pd.Series(["three", "four"])
series3 = series1 + " " + series2
print(series3)					  		 

# compare 2 series using a DataFrame
print ("-" * 10)
vacation2015 = pd.Series([350, 500, 50, 10],
               index=['flight', 'hotel', 'dinner', 'ice cream'])

vacation2016 = pd.Series({'flight': 500, 'hotel': 600, 
                          'dinner': 100, 'ice cream': 15})
                          
# DateFrame needs column head and series
compare_trips = pd.DataFrame({2015: vacation2015,
							  2016: vacation2016})		  
print(compare_trips)
compare_trips = compare_trips.sort_values(2015, ascending=False)
print(compare_trips)
compare_trips['avg'] = 0.5*(compare_trips[2015] + compare_trips[2016])
print(compare_trips)

# DataFrame adding data directly
print ("-" * 10)
presidents = pd.DataFrame([{'name': 'Barack Obama', 
                            'inauguration': 2009, 
                            'birthyear': 1961},
                            {'name': 'GW Bush', 
                            'inauguration': 2001, 
                            'birthyear': 1946},
                            {'name': 'Bill Clinton', 
                            'inauguration': 1993, 
                            'birthyear': 1946}])
print(presidents)
presidents_index = presidents.set_index('name') # reset index to name col                           
print(presidents_index)
# find Bill's inaugration using name index
print(presidents_index.loc['Bill Clinton']['inauguration'])

# create spouce DateFrame
presidents_spouse = pd.DataFrame([{'s1': 'Barack Obama', 's2': 'Michelle Obama'},
								  {'s1': 'GW Bush', 's2': 'Laura Bush'},
								  {'s1': 'Bill Clinton', 's2': 'Hillary Clinton'}])

# connect the 2 DataFrame together
newframe = pd.merge(presidents, presidents_spouse, left_on="name", right_on="s1")
print(newframe)

newframe = pd.merge(presidents, 
                    presidents_spouse, 
                    left_on="name", right_on="s1").drop('s1', axis=1)
print(newframe)














