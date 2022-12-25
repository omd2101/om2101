
def inputs ():                                                 #  input  the  list
    list=[]
    n = int(input("Enter the number of students : "))
    for i in range(n):
        list.append(int(input("Enter the roll number : ")))
    return list

def duplicate(list):                                               # to  remove  duplicate  from  list
    list1=[]
    for i in list:
        if i not in list1:
            list1.append(i)
            
    return list1

def cricket_and_badminton(list1,list2):                           # student who play both cricket and badminton
    list=[]
    for i in list1:
        if i in list2:
            list.append(i)
    print("Students who play both Cricket and Badminton : \n")
    print(list)

def either_or(list1,list2):                                               # student who play either cricket or badminton but not both
    list=[]
    for i in list1:
        if i not in list2:
            list.append(i)
    for i in list2:
        if i not in list1:
            list.append(i)
    print("Students who play either Cricket or Badminton but not both are : \n")
    print(list)

def neither_nor(list1,list2,list3):                                        # students who play neither cricket nor badminton
    list=[]
    for i in list3:
        if i not in list1 and i not in list2:
            list.append(i)
    print("Students who play neither Cricket nor Badminton : \n")
    print(list)

def cricket_football(list1,list2,list3):                                   # students who play cricket and football but not badminton
    list=[]
    new=[]
    for i in list1:
        list.append(i)
    for i in list3:
        list.append(i)
    list=duplicate(list)
    for i in list:
        if i not in list2:
            new.append(i)
    print("Students who play Cricket and Football but not Badminton are : \n")
    print(new)

print("Input for students who play cricket : ")
cricket = inputs()

print("Input for students who play Badminton : ")
badminton = inputs()

print("Input for students who play football : ")
football = inputs()
ch=0
while(ch!=6):
    print("1 . Display the lists ")
    print("2 . Display the students who play both Cricket and Badminton ")
    print("3 . Display students who play Either Cricket or Badminton but not both")
    print("4 . Display students who play neither Cricket nor Badminton ")
    print("5 . Display students who play Cricket anf Football but not Badminton")
    print("6 . Exit")
    print("Enter your choice : ")
    ch=int(input())
    if ch==1:
        print("Cricket : \n",cricket)
        print("Badminton : \n", badminton)
        print("Football : \n", football)
    if ch==2:
        cricket_and_badminton(cricket,badminton)
    if ch==3:
        either_or(cricket,badminton)
    if ch==4:
        neither_nor(cricket,badminton,football)
    if ch==5:
        cricket_football(cricket,badminton,football)
    if ch==6:
        print("Thanks for using the program.")
        break
