import csv

filename = 'googleplaystore.csv'
with open(filename,encoding = "utf8") as f1:
	reader =  csv.reader(f1)
	for line in reader:
		print(line)