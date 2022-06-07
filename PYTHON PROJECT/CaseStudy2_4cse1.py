import csv
import time
import os
import datetime
from prettytable import PrettyTable

filename='4cse1.csv'

# creating file pointer and linking it with csvreader object
csv_read = open(filename,'r')
csvreader=csv.reader(csv_read)

#list initialized that contains the headers
fields=[]
# list initialised that contains all the records 
AllStudents=[] 

fields=next(csvreader,None)
for i in csvreader:
        AllStudents.append(i)

#Fields are : ['URollNo', 'Name', 'DOB', 'City', 'State', 'Marks (CGPA)']


def query1():
        print(" Query 1: To display all the students record from the '4cse1.csv'dataset \n")  
        print("\n Students record of cse1 class: \n")  
        table=PrettyTable(['URollNo','Name','DOB (DD-MM-YYYY)','CITY','STATE','MARKS (CGPA)'])
        for j in AllStudents:
            table.add_row(i)
        print(table)
        print("\n Total number of rows processed: %d"%(csvreader.line_num))


def query2():

    table=PrettyTable(['Name', 'State'])
    print(" Display all the students from a particular state \n ")
    state=input("Enter the state : ")
    for i in AllStudents:
        if i[4] not in(None,''):
            if i[4]==state:
                table.add_row([i[1],i[4]])
    print(table)


def query3():
    print(" Display all students from a particular state and born in a particular month \n" )

    state = input("Enter the state : ")
    month = input("Enter a particular month [January-December] : ")
    table=PrettyTable(['Name','Birth Month'])
    for i in AllStudents:
        m=i[2].split('-')
        datetime_object=datetime.datetime.strptime(m[1],"%m")
        month_name=datetime_object.strftime("%B")

        if i[4] not in (None,''):
            if month_name==month and i[4]==state:
                table.add_row([i[1],i[4]])
    print(table)
               
def query4():
    print(" Display all students with a given CGPA and above \n")
    cgpa=float(input("Enter a CGPA : "))
    table=PrettyTable(['Name','CGPA'])
    for i in AllStudents:
        if i[5] not in(None,''):
            if float(i[5])==cgpa or float(i[5])>cgpa:
                table.add_row([i[1],i[5]])
    print(table)

def query5():
    print("Display all students whose name starts with a particular letter and a particular year of birth \n ")
    letter = input("Enter the first character of the name : ")
    year=int(input('Enter year [example - 2000] :  '))
    table=PrettyTable(['Name','Year of Birth'])
    for i in AllStudents:
        y=i[2].split('-')
        if int(y[2])==year and i[1].startswith(letter):
            table.add_row([i[1],y[2]])
    print(table)

if os.name == 'posix':
    operating_system = "linux"
else:
    operating_system = "windows"

def ClearScreen():
    if operating_system.upper() == "LINUX":
        os.system('clear')
    else:
        os.system('cls')

while(True):
    print("""
    1.Display all students.\n
    2.Display all the students from a particular state \n
    3.Display all students from a particular state and born in a particular month \n
    4.Display all students with a given CGPA \n
    5.Display all students whose name starts with a particular letter and a particular year of birth \n
    6.Exit \n """)
    
    choice = int(input("Enter Your Choice (1-6) : "))

    if choice==1:
        ClearScreen()
        query1()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
        #clear()
    elif choice==2:
        ClearScreen()
        query2()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
    elif choice==3:
        ClearScreen()
        query3()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
    elif choice==4:
        ClearScreen()
        query4()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
    elif choice==5:
        ClearScreen()
        query5()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
    else:
        ClearScreen()
        print("Exit")
        input("\n\n ------ Press enter to continue  ---------")
        exit()
        
# csv_read.close()
