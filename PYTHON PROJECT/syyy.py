import csv
# import pandas as pd
def searchbyname():
	print("	\n")
	print("Enter 1 to know the count of App : ")
	print("Enter 2 to know the Details of App you Entered : ")
	ch1 = int(input("Enter your Choice : "))
	if ch1==1:
		with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
			reader = csv.reader(f1)
			name = str(input("Enter the name of app for which you want count : "))
			lineread=0
			for row in reader:
				if name in row[0]:
					lineread+=1
			print(f"the app with name = {name} is Appeared {lineread} Times")
			searchbyname()
	elif ch1==2:
		with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
			print("Please use firstletter CAPITAL and REST Small")
			name = str(input("Enter App Name : "))
			print(" OK....YOU Entered this Name? : " +name , " ")
			reader = csv.reader(f1)
			choice = int(input(" Enter 1 for YES or 2 for NO : " ))
			if choice == 1:
				for row in reader:
					if name in row[0]:
						print(row)
			else:
				searchbyname()	
def searchbysize():
	print("	\n")
	print("PLease Note :- THE MAXIMUM SIZE IS 100M")
	print("Enter 1 to know the count of : ")
	print("Enter 2 to know the Details of App you Entered : ")
	ch1 = int(input("Enter your Choice : "))
	size = str(input("Enter App Size : "))
	with open('googleplaystore.csv',encoding="utf8") as f1:
		reader = csv.reader(f1)
		for row in reader:
			if size in row[4]:
				print(row)
def searchbytype():
	try:
		print("\n")
		print("THERE ARE TWO TYPE OF APPS HERE:\n1.Paid \n2.Free")
		print("\n")
		print("PRESS 1 FOR 'FREE' APPS \nPRESS 2 FOR 'PAID' APPS")
		print("Press 3 to Return to MAIN MENU")
		print("Press 4 to know total FREE apps")
		print("Press 5 to know total PAID apps")
		typi = int(input("Enter your option : "))
		with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
			reader = csv.reader(f1)
			if typi==1:
				try:
					for row in reader:
						if row[6] == "Free":
							print(row)
				except ValueError as e:
					print("please enter valid input")
					searchbytype()
			if typi==2:
				try:
					for row in reader:
						if row[6] == "Paid":
							print(row)
				except ValueError as e:
					searchbytype()
			if typi==3:
				menu()
			if typi==4:
				with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
					reader = csv.reader(f1)
					lineread=0
					for row in reader:
						if row[6] == "Free":
							lineread+=1
					print(f"THERE ARE {lineread} FREE Apps in the list")
			if typi==5:
				with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
					reader = csv.reader(f1)
					lineread=0
					for row in reader:
						if row[6] == "Paid":
							lineread+=1
					print(f"THERE ARE {lineread} PAID Apps in the list")
	except ValueError as e:
		searchbytype()
def category():
        print("\n")
        print("There Are Many Categories")
        print("Enter 1 to know the count of Category : ")
        print("Enter 2 to know the Details of cATEGORY you Entered : ")
        choicew = int(input("Enter Your Choice : ")
        	if choicew==1:
		with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
			reader = csv.reader(f1)
			name = str(input("Enter the Category of app for which you want count : "))
			lineread=0
			for row in reader:
				if choicew in row[1]:
					lineread+=1
			print(f"the app with CATEGORY = {choicew} is Appeared {lineread} Times")
			category()
        if choicew==2:
        	with open('C:/Users/91884/Documents/PYTHON PROJECT/googleplaystore.csv',encoding="utf8") as f1:
        		try:
        			print("Please ENTER CAPITAL LETTERS ONLY ")
        			name = str(input("Enter CATEGORY : "))
        			print(" OK....YOU Entered CATEGORY = " +name , " ?")
        			reader = csv.reader(f1)
        			choicew = int(input(" Enter 1 for YES or 2 for NO : " ))
        			try:
        				if choice == 1:
        					for row in reader:
        						if choicew in row[1]:
        							print(row)
        				else:
        					print("We are Redirecting you to Category Option..")
        					category()
        			except ValueError as e:
        				print("Please enter valid value")
        				category()
        		except ValueError as e:
        			category()
def menu():
	print("\n")
	try:
		print("Enter 1 to search by app size : ")
		print("Enter 2 to search by type : ")
		print("Enter 3 to search by Name : ")
		print("Enter 4 to search by Category : ")
		src = int(input("ENTER YOUR CHOICE : "))
		if src==1:
			searchbysize()
		elif src==2:
			searchbytype()
		elif src==3:
			searchbyname()
		elif src==4:
			category()
		else:
			print("\n")
			print("please enter a vlaif value")
			menu()
	except ValueError as e:
		print("Please enter Correct Given Options\n")
		menu()
menu()
