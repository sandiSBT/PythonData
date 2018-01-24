import csv 
f = open('daily_show_guests.csv')
csv_f = csv.reader(f)
for row in csv_f:
	print(row)