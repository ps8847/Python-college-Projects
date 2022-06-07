import csv
with open(r"C:\Users\Pritpal Singh\Desktop\coding files\googleplaystore.csv",encoding=" utf8") as csv_file:
    csv_reader=csv.reader(csv_file)
    header=next(csv_reader)
    r=[]
    for i in csv_reader:
        r.append(i)
        #print(i)
1 #Display APP name having install more than 50,000 and famous in teen and is Paid
    for i in r:
        a=i[5][:-1]
        a=a.split(",")
        a=''.join(a)
        a=int(a)
        if a>= 50000 and i[8]=='Teen' and i[7]!='0':
            print(i[0],i[5],i[8],i[7])
2 '''#check how many apps have installs more than 1B
    for i in r:
        a=i[5][:-1]
        a=a.split(",")
        a=''.join(a)
        a=int(a)
        if a>= 1000000000:
            print(i[0],i[3])'''       
        
    #to display app with hightest price
    

 3   '''#check if app name contains CAmera in it
    c=0
    for i in r:
        if 'camera' in i[0] or 'Camera' in i[0]:
            print(i[0])
            c+=1
    print(c)'''
    
# Display all the data of the file.
    #for i in csv_reader:
        #r.append(i)
        #print(i) 
4 #Display the names and rating of the apps having rating more than 4.8.
    #for i in r:
       #if i[2] not in (None,'NaN'):
          #if (i[2])>str(4.8):
             #print(i[0],i[2])


5 #Display the name of the having no of reviews = 159
     
   # for i in r:
        #if (i[3])==str(159):
            # print(i[0],i[3])
6 #Display the names and rating of the apps having EDUCATION  as their genre and rating of 5.
   # for i in r:
        #if i[9]=='Education' and i[2]==str(5):
            #print(i[0],i[2],i[9])


7 # Display the name and of the apps which are popular in Teen
   # c=0
   #  for i in r:
    
   #      if i[8]=='Teen':
   #           c+=1
   #           print(i[0],i[8])
   #  print(c)         

8'''#count paid apps
    c=0
    for i in r:
        if i[6]=="Paid":
            c+=1
    print(c)'''

9 #Display app name whose size,current version & android version varies with device
    # for i in r:
    #     if i[4]=='Varies with device' and i[11]=='Varies with device' and i[12]=='Varies with device':
    #         print(i[0])
    
10 #DISPLAY app Names having price more than $10 and rewiers more than 1000
    

    

