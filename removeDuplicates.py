def remove_dup(li):
    u=[]
    d=[]
    for i in li:
        if i not in u:
            u.append(i)
        else:
            d.append(i)
    return u
li=[6]
print(li)
print(remove_dup(li))
