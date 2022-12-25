students_attend = []
n = int(input("Enter the total no. of students who attended the training program. "))
print("Enter the roll no. of students who attended the training program. ")
for i in range(n):
    students_attend.append(int(input()))

search_element = int(input("Enter the roll no. that you want to search : "))

def linear_search(students_attend, search_element):
    for i in students_attend:
        if i == search_element:
            return 1
    return -1


def sentinel_search(students_attend, search_element, n):
    last = students_attend[n-1]
    students_attend[n-1] = search_element
    i= 0
    while(students_attend[i]!=search_element):
        i = i +1
    students_attend[n-1] = last
    if(students_attend[n-1]==search_element  or i<n-1):
        return 1
    return -1

print("1) Linear search")

print("2) Sentinal search")
ch = int(input("Enter your choice "))

if ch == 1:
    result = linear_search(students_attend, search_element)
    if result == -1:
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

elif ch == 2:
    result = sentinel_search(students_attend, search_element, n)
    if result == -1:
        print("The entered roll no. did not attend the training program.")
    else:
        print("The entered roll no. has attended the training program.")

else:
    print("Sorry wrong choice")









list=[]
n=int(input("Enter the Number of elements : "))
for i in range(n):
    list.append(int(input("Enter the element : ")))
print("List : ",list)


def binary(l,q):
    n=len(l)
    l1=0
    h=n-1
    flag =0
    while(l1<=h):
        mid=(l1+h)//2
        if l[mid]==q:
            print(mid)
            flag=1
            break
        elif q<l[mid]:
            h=mid-1
        else:
            l1=mid+1
    if flag == 0:
        print("Not present")


ch=-1
while ch!=2:
    ch=int(input("Enter your choice : "))
    if(ch==2):
        break
    key = int(input("Enter the eky for search : "))
    binary(list,key)





def fibonacci(l,k):
    n=len(l)
    f0=0
    f1=1
    f2=1
    offset=-1

    while(f2<n):
        f0=f1
        f1=f2
        f2=f1+f0

    while(f2>1):
        i=min(offset+f0,n-1)
        if(key<l[i]):
            f2=f0
            f1=f1-f0
            f0=f2-f1
        elif(key>l[i]):
            f2=f1
            f1=f0
            f0=f2-f0
            offset=i
        else:
            return i
    if(l[n-1]==key):
        return n-1
    return -1

print(fibonacci(list,key))