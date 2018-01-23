# lists.py

"""
This is my python project
I want to add multiple lines

"""

'''
YES YOU CAN!
'''

print 'Python is working'
print "Python is still working"
year = 2016
print year
class_name = "Python"
print "we're taking a", class_name, "class"
cities = ['New York', 'London', 'San Francisco']
print cities
print cities[1]
print len(cities)
print len(class_name)
# This is a loop - all of the statements in loop are 
		# indented!
for i in range(3):
	print cities[i]
	print 'i am printing'
	print 'something else'
	print 'again'
for i in cities:
	print i

cities.extend(['Detroit', 'Cleveland'])
print cities
world_cities = cities + ['Tokyo', 'Santiago']
print world_cities
# do this without mutating - stay tuned!
#new_list = world_cities.insert(1, 'Los Angeles')
#world_cities.insert(1, 'Los Angeles')
del world_cities[3]
print len(world_cities)

for i in range(6):
	print world_cities[i]
	
for i in world_cities:
	print i
world_cities.insert(1, 'Los Angeles')
print world_cities

world_cities.remove('London')
print world_cities
print world_cities[0]
print world_cities[0:2]
print world_cities[:3]

names = ['Rachel', 'Jenna', 'Stacy', 'Michelle']
print names[2:]
print names[2:4]
print names[1:3]
print names[:3]
print names[-2] # second to last item
print names[-1] # last item




























