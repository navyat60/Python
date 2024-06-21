def is_sorted(li):
    flag=0
    for i in range(1,len(li)):
        if(li[i]<li[i-1]):
            flag=1
    if flag==0:
        print("array is sorted ")
    else:
        print("not sorted")


li=[]
n=int(input("Enter the number of elements "))
for i in range(0,n):
    el=int(input())
    li.append(el)

print(li)
#li.sort()
is_sorted(li)

#print(li)