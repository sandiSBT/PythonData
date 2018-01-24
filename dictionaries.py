# dict can use anything to access the items
# key:value
# dict has no order, can't ask for position 3
# use key or value to access data
# used for lookup tables


presidents = {
	"first": "George Washington",
	"second": "John Adams",
	"third": "Thomas Jefferson"
}

data = [{
	'name': 'george washington',
	'age': 57,
	'teeth': 'wooden'
},
{
	'name': 'john adams',
	'age': 57,
	'teeth': 'unknown'
}
]
print(presidents["second"])
presidents["fourth"] = "James Madison"
print(presidents["fourth"])
print(presidents) # no order
print("fourth" in presidents) # Test to see if key in dic
print("pancakes" in presidents)

# ways to work with dics
for key in presidents:
	print(key)
	
for value in presidents.values():
	print(value)	

print(presidents.values()) # list of values
print(presidents.keys()) # list of keys

for number, name in presidents.items():
	print(number, name)

print(presidents.items())
for key in sorted(presidents):
	print (key, presidents[key])
	
print(presidents['fourth'])
# print presidents[key]
print(sorted(presidents))
for k, v in sorted(presidents.items()):
	print(k, v)

print(sorted(presidents.values()))
# ['George Washington', 'James Madison', 'Thomas Jefferson', 'Zohn Adams']
print(sorted(presidents.items()))		

# along with dictionaries you can create lists of lists
# split phrase into inital list
words = "Ask not what your country can do for you".split()
print(words)

# create a list that contains 3 col of lists
builder = [[w.upper(), w.lower(), len(w)] for w in words]
print(builder) # Builds a list of lists

for i in builder:
	print(i) # Prints all list items (which are lists)

for i in builder: 
	print(i[0])	# prints col 0 of list - upper case words

animals = {
	'Dave': 'cow',
	'Frank': 'cat',
	'Bill': 'kangaroo'
}	

print(animals)
animal_transform = {animals[k]: k for k in animals}
print(animal_transform)


# nesting list and dic inside a dictionary
course = {
	'name': "Python",
	'location': "Stanford",
	'temperature': "cold",
	'computers': ["mac", "pc"],
	'teacher': {
		'first_name': "Jane",
		'last_name': "Doe"
	}
}

print(course.keys(), course['teacher'].keys())
print(course.values(), course['teacher'].values())
print(course['computers'][1])
print(course['teacher']['last_name'])

# Dictionaries & Comprehensions
uppercased = [[c.upper()] for c in course['computers']]
print(uppercased)

# simplified
uppercased = [c.upper() for c in course['computers']]



























