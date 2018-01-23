cities = ['San francisco', 'tahoe city']

presidents = {
	"first": "George Washington",
	"second": "Zohn Adams",
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
print presidents["second"]
presidents["fourth"] = "James Madison"
print presidents["fourth"]
print presidents 
print "fourth" in presidents
print "pancakes" in presidents

for key in presidents:
	print key
	
for value in presidents.values():
	print value	

print presidents.values()
print presidents.keys()
for number, name in presidents.items():
	print number, name
print presidents.items()
for key in sorted(presidents):
	print key, presidents[key]
print presidents['fourth']
# print presidents[key]
print sorted(presidents)
for k, v in sorted(presidents.items()):
	print k, v

print sorted(presidents.keys());
# ['George Washington', 'James Madison', 'Thomas Jefferson', 'Zohn Adams']
print sorted(presidents.items())		

words = "Ask not what your country can do for you".split()
print words
builder = [[w.upper(), w.lower(), len(w)] for w in words]
print builder # Builds a list of lists

for i in builder:
	print i # Prints all list items (which are lists)

for i in builder: 
	print i[0]	

animals = {
	'Dave': 'cow',
	'Frank': 'cat',
	'Bill': 'kangaroo'
}	

animal_transform = {animals[k]: k for k in animals}
print animal_transform

course = {
	'name': "Python",
	'location': "Stanford",
	'temperature': "cold",
	'computers': ["mac", "pc"],
	'teacher': {
		'first_name': "Eve",
		'last_name': "Porcello"
	}
}

print course.keys(), course['teacher'].keys()
print course.values(), course['teacher'].values()
print course['computers'][1]
print course['teacher']['last_name']

# Dictionaries & Comprehensions
uppercased = [[c.upper()] for c in course['computers']]
print uppercased
uppercased = [c.upper() for c in course['computers']]



























