list1 = []
x= (int)(input("enter no of row :"))
y = (int)(input("enter no of column :"))
print("\nenter element of first matrix")
for i in range(x):
    list = []
    for j in range(y):
        list.append(int(input("enter no : ")))
    list1.append(list)
print("\nmatrix a = :")
for i in range(x): 
    print("\n")
    for j in range(y):
        print(list1[i][j],end=" ")

print("\nenter element of second matrix")
list3 = []
for i in range(x):
    list2 = []
    for j in range(y):
        list2.append(int(input("enter no : ")))
    list3.append(list2)
print("\nmatrix 2 = :")
for i in range(x):
    print("\n")
    for j in range(y):
        print(list3[i][j],end=" ")
print("\n")

add1 = []
def add(a,b):
    for i in range(x):
        sum =[]
        for j in range(y):
            sum.append(int(a[i][j] + b[i][j]))
        add1.append(sum)
    print("\naddition = :")
    for i in range(x): 
        print("\n")
        for j in range(y):
            print(add1[i][j],end=" ")

sub1 = []
def sub(a,b):
    for i in range(x):
        sub =[]
        for j in range(y):
            sub.append(int(a[i][j] - b[i][j]))
        sub1.append(sub)
    print("\nsubtraction = :")
    for i in range(x): 
        print("\n")
        for j in range(y):
            print(sub1[i][j],end=" ")

def mult(a,b):
    mul = [[0 for e in range(3)]for r in range(3)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                mul[i][j]+=(a[i][k]*b[k][j])
    print("\nmultiplication of matrix is = :")
    for i in range(x): 
        print("\n")
        for j in range(y):
            print(mul[i][j],end=" ")

def transpose(a,x,y):
        print("\nmatrix a = :")
        for i in range(x): 
            print("\n")
            for j in range(y):
                print(a[j][i],end=" ")
        if x!=y:
            print("transpose imposible enter value of x=y :")

print(" 1. perform addition\n")
print(" 2. perform subtration\n")
print(" 3. perform multiplication\n")
print(" 4. perform transpose")
m=1
while(m<=5):
    l=int(input("\nenter your choice\n"))
    if l==1:
        add(list1,list3)
    if l ==2:
        sub(list1,list3)
    if l==3:
        mult(list1,list3)
    if l==4:
        transpose(list1,x,y)
    m=m+1