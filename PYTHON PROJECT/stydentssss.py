import csv
def menu():
  print("\n")
  print("Case Study 1: Student Database")
  print('''\t\tPress 1 to Print all Student's Data
  \t\tPress 2 to Display all the students from a particular state/country
  \t\tPress 3 to Display all students from a particular state and born in a particular month
  \t\tPress 4 to Display all students with given CGPA
  \t\tPress 5 to Display all students whose name starts with a particular letter and a particular year of birth
  \t\tPress 6 to EXIT THE APPLICATION''')
  try:
    n = int(input("Enter Your Choice : "))
    if n==1:
      printstudents()
    elif n==2:
      statecountry()
    elif n==3:
      monthstate()
    elif n==4:
      cgpa()
    elif n==5:
      namestart()
    elif n==6:
      quit()
    else:
      print("Invalid Input,,,Please Choose A Valid Option")
      menu()
  except ValueError as e:
    print("Invalid Input,,,Please Choose A Valid Option")
    menu()
def printstudents():
  f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
  csvreader = csv.reader(f)
  header = next(csvreader)
  for i in csvreader:
    print(i)
  print("\n")
  print("Hope You Are Satisfied With The Result\nWe Are Redirecting You to main menu")
  print("\n")
  menu()
  #Display all the students from a particular state/country
def statecountry():
  try:
    f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    flag = 0
    print("PLEASE NOTE :- ENTER FIRST LETTER CAPITAL REST SMALL")
    n=input("Enter the name of the State/Country : ")
    for i in csvreader:
      if i[5] == n:
        print(i[0])
        flag = 1
    if flag==0:
      print(f"there is no student from {n}")
      option2()
    option2()
  except ValueError as e:
    print("Please Enter Valid Value")
    option2()
#Display all students from a particular state and born in a particular month
def monthstate():
  try:
    f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    print('''PLEASE NOTE :- ENTER FIRST LETTER CAPITAL REST SMALL for STATE''')
    print('''PLEASE NOTE :- IN MONTH ENTER ONLY INTEGERS VALUES....for Example:-
             ENTER 1 for month JANUARY
             ENTER 2 for month FABRUARY   and so on...''')
    flag = 0
    n = input("Enter State : ")
    p = input("Enter Month : ")
    for i in csvreader:
      if i[5] == n and i[3][3] == p:
        print(f"{i[0]} is the Student from {n} and having DOB month {p} ")
        flag=1
      elif i[5] == n and i[3][2] == p:
        print(f"{i[0]} is the Student from {n} and having DOB month {p} ")
        flag=1
      elif i[5] == n and i[2:3] == p:
        print(f"{i[0]} is the Student from {n} and having DOB month {p} ")
        flag=1
      elif i[5] == n and i[3:4] == p:
        print(f"{i[0]} is the Student from {n} and having DOB month {p} ")
        flag = 1
    if flag == 0:
      print(f"There is No Student from {n} having DOB Month as {p}")
      option3()
    option3()
  except ValueError as e:
    print("Please Enter Valid input")
    monthstate()

#Display all students with a given CGPA    
def cgpa():
  f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
  csvreader = csv.reader(f)
  header = next(csvreader)
  try:
    flag = 0
    n=eval(input("Enter CGPA : "))
    for i in csvreader:
      if  int(i[6])== n:
        print(f"{i[0]} has Scored {n} CGPA in Last Semester")
        flag =1
    if flag == 0:
      print(f"No Student has Scored {n} CGPA")
      option4()
    option4()
  except Exception as e:
    print("Please Enter Valid input")
    cgpa()

#Display all students whose name starts with a particular letter and a particular year of birth
def namestart():
  f = open(r"C:/Users/91884/Documents/PYTHON PROJECT/sd1.csv","r")
  csvreader = csv.reader(f)
  header = next(csvreader)
  print('''INSTRUCTIONS TO USE THIS FEATURE

          1. Enter Only Capital Letter for First Character Of The Name
          2. Enter DOB in Given Format Only
            (i)   --/-/----
            (ii)  --/--/----
            (iii) -/-/----
            (iv)  -/--/----''')
              
  flag = 0
  n=input("Enter First Character Of The Name : ")
  p=input("Enter DOB : ")
  for i in csvreader:
    if i[0].startswith(n) and i[3][0:10] == p:
        print(f'''{i[0]} is the Student whose Name is Starting with Letter '{n}' and Having DOB as '{p}' ''')
        flag =1
  if flag == 0:
    print(f'''There is No Student's Name is Starting with '{n}' and having DOB as '{p}' ''')
    option4()
  option4()
def option2():
  print("\n")
  print("If You Want To Go To MAIN MENU PRESS 1: ")
  print("If You Want To Perform Previous Task PRESS 2: ")
  try:
    nn = int(input("Enter Your CHOICE : "))
    if nn==1:
      menu()
    elif nn==2:
      statecountry()
  except ValueError as e:
    print("INVALID INPUT.......WE ARE Redirecting YOU TO MAIN MENU")
    menu()
def option3():
  print("\n")
  print("If You Want To Go To MAIN MENU PRESS 1: ")
  print("If You Want To Perform Previous Task PRESS 2: ")
  try:
    nn = int(input("Enter Your CHOICE : "))
    if nn==1:
      menu()
    elif nn==2:
      monthstate()
  except ValueError as e:
    print("INVALID INPUT.......WE ARE Redirecting YOU TO MAIN MENU")
    menu()
def option4():
  print("\n")
  print("If You Want To Go To MAIN MENU PRESS 1: ")
  print("If You Want To Perform Previous Task PRESS 2: ")
  try:
    nn = int(input("Enter Your CHOICE : "))
    if nn==1:
      menu()
    elif nn==2:
      cgpa()
  except ValueError as e:
    print("INVALID INPUT.......WE ARE Redirecting YOU TO MAIN MENU")
    menu()
def option5():
  print("\n")
  print("If You Want To Go To MAIN MENU PRESS 1: ")
  print("If You Want To Perform Previous Task PRESS 2: ")
  try:
    nn = int(input("Enter Your CHOICE : "))
    if nn==1:
      menu()
    elif nn==2:
      namestart()
  except ValueError as e:
    print("INVALID INPUT.......WE ARE Redirecting YOU TO MAIN MENU")
    menu()
menu()

