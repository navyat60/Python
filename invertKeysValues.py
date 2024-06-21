def invert_content(dic):
    invert_dec={}
    invert_dec={k:v for v,k in dic.items()}
    return invert_dec
n=int(input("no of val:"))
dic={}
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dic[key]=value
print(dic)
print(invert_content(dic))