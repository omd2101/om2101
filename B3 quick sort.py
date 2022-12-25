def swap(a,b,list):
    temp=list[a]
    list[a]=list[b]
    list[b]=temp

def partition(list,start,end):
    pivot=start
    piele=list[pivot]
    while start < end :
        while list[start] <= piele :
            start +=1
        while list[end] > piele :
            end -=1
        if start < end:
            swap(start,end,list)

    swap(pivot,end,list)
    return end

def sort(list,start,end):
    if start < end:
        pi=partition(list,start,end)
        sort(list,start,pi-1)
        sort(list,pi+1,end)

list1 = []
n=int(input("enter number of elements"))
for i in range(n):

    list1.append(int(input("enter element")))
sort(list1,0,len(list1)-1)
print(list1)