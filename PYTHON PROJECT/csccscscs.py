import csv
with open('googleplaystore.csv','r') as f1:
			reader = csv.reader(f1)
			name = str(input("Enter the name of app for which you want count : "))
			lineread=0
			for row in reader:
				if name in row[0]:
					lineread+=1
				print(f"the app with name = {name} is Appeared {lineread} Times")