import csv
f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
csvreader = csv.reader(f)
header = next(csvreader)

def start():
  print("Case Study 1: Student Database")
  choice = int(input(''' \t\t1. Printing all Student's Data
                2. Display all the students from a particular state/country
                3. Display all students from a particular state and born in a particular month
                4. Display all students with given CGPA
                5. Display all students whose name starts with a particular letter and a particular year of birth
                Now Enter your Choice : '''))
  return choice

choice=start()
#List all the student's data
if choice == 1: 
  for i in csvreader:
    print(i)

#Display all the students from a particular state/country
elif choice == 2:
  flag = 0
  n=input("Enter  the name of the State/Country : ")
  for i in csvreader:
    if i[5] == n:
      print(i[0])
      flag = 1
  if flag == 0:
    print("Invalid Input")

#Display all students from a particular state and born in a particular month
elif choice == 3:
  flag = 0
  n = input(" enter  state")
  p = input(" enter month")
  for i in csvreader:
    if i[5] == n and i[3][3:5] == p:
        print(i[0])
        flag = 1
  if flag == 0:
    print("Invalid Input")

#Display all students with a given CGPA    
elif choice == 4:
  flag = 0
  n=eval(input("Enter CGPA : "))
  for i in csvreader:
    if  int(i[6])== n:
      print(i[0],i[6])
      flag =1
  if flag == 0:
    print("Invalid Input")

#Display all students whose name starts with a particular letter and a particular year of birth
elif choice == 5:
  flag = 0
  n=input("Enter Char : ")
  p=input("Enter DOB : ")
  for i in csvreader:
    if i[0].startswith(n) and i[3][6:] == p:
        print(i[0])
        flag =1
  if flag == 0:
    print("Invalid Input")

else:
  print("Input Invalid")
