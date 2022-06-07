import csv
with open(r"C:\Users\91884\Documents\PYTHON PROJECT\googleplaystore.csv",encoding=" utf8") as csv_file:
    csv_reader=csv.reader(csv_file)
    header=next(csv_reader)
    r=[]
    for i in csv_reader:
        r.append(i)
        #print(i)
    for i in r:
        a=i[7]
        b=a.replace('$','')
        a=int(b)
        print(b)
#Display APP name having install more than 50,000 and famous in teen and is Paid
    #for i in r:
        #a=i[5][1]
        #a=a.split(",")
        #a=''.join(a)
        #a=int(a)
        #if a>= 50000 and i[8]=='Teen' and i[7]!='0':
            #print(i[0],i[5],i[8],i[7])

#Display app name whose size,current version & android version varies with device
    #for i in r:
       # if i[4]=='Varies with device' and i[11]=='Varies with device' and i[12]=='Varies with device':
            #print(i[0])
    #for i in r:
        #a=i[5][:-1]
        #a=a.split(",")
        #a=''.join(a)
        #a=int(a)
        #if a>= 1000000000:
            #print(i[0],i[3])

