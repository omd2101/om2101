list=[]
n=int(input("Enter total no of student : "))
for i in range(n):
    list.append(int(input("Enter the element : ")))
print("List : ",list)

def linear_search(students_attend, search_element):
    for i in students_attend:
        if i == search_element:
            return 1
    return -1


def sentinel_search(students_attend, search_element):
    n = len(students_attend)
    last = students_attend[n-1]
    students_attend[n-1] = search_element
    i= 0
    while(students_attend[i]!=search_element):
        i = i +1
    students_attend[n-1] = last
    if(students_attend[n-1]==search_element  or i<n-1):
        return 1
    return -1

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

def fibonacci(l,q):
    n=len(l)
    f0=0
    f1=1
    f2=1
    offset=-1
    flag=0
    while(f2<n):
        f0=f1
        f1=f2
        f2=f1+f0
    while(f2>1):
        i=min(offset+f0,n-1)
        if l[i]==q:
            print(i)
            flag=1
            break
        elif l[n-1]==q:
            print(n-1)
            flag=1
            break
        elif l[i]>q:
            f2=f0
            f1=f1-f2
            f0=f2-f1
        else:
            f2=f1
            f1=f0
            f0=f2-f1
            offset=i
    if flag==0:
        print("Not found")


choic =int(input("enter 1"))
while(choic<5):
    print("1. bynary search ")
    print("\n2. fibunacci search\n ")
    print("3 Linear search\n")
    print("4 Sentinal search\n")
    choice =int(input("enter choice"))
    if choice == 1:
        key = int(input("Enter the eky for search : "))
        binary(list,key)

    if choice == 2:
        key = int(input("Enter the eky for search : "))
        fibonacci(list,key)

    if choice == 3:
        key = int(input("Enter the eky for search : "))
        result = linear_search(list,key)
        if result == -1:
            print("The entered roll no. did not attend the training program.")
        else:
            print("The entered roll no. has attended the training program.")

    elif choice == 4:
        key = int(input("Enter the eky for search : "))
        result = sentinel_search(list,key)
        if result == -1:
            print("The entered roll no. did not attend the training program.")
        else:
            print("The entered roll no. has attended the training program.")