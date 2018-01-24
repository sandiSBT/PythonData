# lists.py

# Review comments, print, variables

"""
This is my python project
I want to add multiple lines

"""

'''
YES YOU CAN!
'''

print('Python is working')
print("Python is still working")
year = 2016
print(year)
class_name = "Python"
print("we're taking a", class_name, "class")

# create list
cities = ['New York', 'London', 'San Francisco']
print(cities)
print(cities[1]) # list 0-based
print(len(cities)) # num of items in array
print(len(class_name)) # len of data in var

# This is a loop - all of the statements in loop are 
		# indented!
print ('-' * 10)		
for i in range(3):
	print(cities[i])
	print('i am printing')
	print('something else')
	print('again')

print('-' * 10)
for i in cities:
	print(i)

# adding to the list
cities.extend(['Detroit', 'Cleveland'])
print(cities)

world_cities = cities + ['Tokyo', 'Santiago']
print(world_cities)
# do this without mutating - stay tuned!
#new_list = world_cities.insert(1, 'Los Angeles')
#world_cities.insert(1, 'Los Angeles')

del world_cities[3]
print(len(world_cities))

for i in range(6):
	print(world_cities[i])
	
for i in world_cities:
	print(i)
world_cities.insert(1, 'Los Angeles')


world_cities.remove('London')
print(world_cities)
print(world_cities[0])
print(world_cities[0:2])
print(world_cities[:3])

# Practice: Make another list, print ranges
names = ['Rachel', 'Jenna', 'Stacy', 'Michelle','Wendy','Mary','Dana']
print(names[2:]) # start position : stop position not included in output
print(names[2:4])
print(names[1:3])
print(names[:3])
print(names[-2]) # second to last item
print(names[-1]) # last item




























