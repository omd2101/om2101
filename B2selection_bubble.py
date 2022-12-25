list=[]
n=int(input("Enter the size of array : "))
for i in range(n):
    list.append((int(input("Enter the element : "))))

def selection(l):
    n = len(l)
    i=0
    while(i<n-1):
        j=i
        k=i
        while(j<n):
            if l[k]>l[j]:
                temp=l[k]
                l[k]=l[j]
                l[j]=temp
            j+=1

        temp=l[i]
        l[i]=l[k]
        l[k]=temp

        i+=1

    print(l)

def bubble(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-1-i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    print(l)



selection(list)
bubble(list)