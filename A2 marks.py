mark=[]
n=int(input("Enter the number of students : "))
for i in range(n):
    mark.append(int(input("Enter the marks : ")))

def average(list):
    sum=0
    for i in list:
        if i!=-1:
            sum+=i
    print("Average marks of class are : ",sum/len(list))

def highlow(list):
    high=list[0]
    low=list[0]
    for i in list:
        if high<i:
            high=i
        if low>i and i>=0:
            low=i
    print("Highest is : ",high)
    print("Lowest is : ",low)

def absent(list):
    count=0
    for i in list:
        if i==-1:
            count+=1
    print("Number of absent students are : ",count)

def freq(list):
    high=list[0]
    for i in list:
        if high<i:
            high=i
    count=0
    for i in list:
        if i==high:
            count+=1
    print("Highest frequency is : ",count)

ch=0
while(ch!=6):
    print("1 . Display marks")
    print("2 . Display average")
    print("3 . Display highest and lowest")
    print("4 . Display absent")
    print("5 . Display highest frequency")
    print("6 . Exit")
    ch=int(input("Enter the choice : "))
    if ch==1:
        print("Marks list is : \n",mark)
    if ch==2:
        average(mark)
    if ch==3:
        highlow(mark)
    if ch==4:
        absent(mark)
    if ch==5:
        freq(mark)
    if ch==6:
        print("Thanks for using this program.")
        break