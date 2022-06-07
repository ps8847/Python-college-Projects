import csv
import os
from prettytable import PrettyTable

filename='Dataset-movies1.csv'

# creating file pointer and linking it with csvreader object
csv_read = open(filename,'r')
csvreader=csv.reader(csv_read)

#fields=['S.No   Movie Name       Release Year    Rating    Runtime(in seconds)']

# list initialised that contains all the records 
movies=[] 
for i in csvreader:
        movies.append(i)
    

def query1():
    print("1. List the movie names and release year of all the movies released after 1990 and do not have a null in the rating \n ")
    table=PrettyTable(['Movie Name','Release Year'])
    for i in movies:
        if i[3] not in (None,''):
            if int(i[2]) > 1990:
                table.add_row([i[1],i[2]])
    
    # Displaying first 15 records
    print(table.get_string(start=0,end=15))        

def query3():
    print("List all movie names and release year for the movie names beginning with ‟A” and rating is not null and release year is not between 1980 and 1995.")    
    table=PrettyTable(['Movie Name','Release Year(<1980 and >2000',])
    for i in movies:
        if i[2] not in ( None,'') and i[3] not in (None,''):
            if i[1].startswith('A'):
                if  int(i[2])<1980 or int(i[2])>1995:
                    table.add_row([i[1],i[2]])
    # Displaying first twenty records
    print(table.get_string(start=0,end=20))

def query2():
    print("List the movie names and rating of all movies in which movie name contains the word 'boys' or the word 'wild' ")
    table=PrettyTable(['Movie Name','Rating'])
    for i in movies:
        if i[3] not in (None,''):
            if i[1].count("boys") or i[1].count("wild")>=1:
                table.add_row([i[1],i[3]])
    print(table)

def query4():
    print("Count the number of movies released in the year 1989 and duration is more than 1.5 hours.")
    table=PrettyTable(['Movie name','Duration'])
    for i in movies:
        if i[4] not in (None,''):
            # print(type(i[2]))
            if int(i[2])==1989 and int(i[4])>5400:
                table.add_row([i[1],i[4]])
    # Displaying first ten records            
    print(table.get_string(starts=0,end=10))

# Clear screen defination

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
    1. List the movie names and release year of all the movies released after 1990 and do not have a null in the rating
    2. List the movie names and rating of all movies in which movie name contains the word “boys” or the word “wild”.
    3. List all movie names and release year for the movie names beginning with ‟A”,rating is not null and 
       release year is not between 1980 and 1995.
    4. Count the number of movies released in the year 1989 and duration is more than 1.5 hours.
    5.Exit \n """)
    
    choice = int(input("Enter Your Choice (1-6) : "))

    if choice==1:
        ClearScreen()
        query1()
        input("\n\n ------ Press enter to continue  ---------")
        ClearScreen()
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
        
csv_read.close()