def duplicate(self,list1):
    new_value=set(list1)
    if len(new_value)==len(list1):
        return 'false'
    else:
        return 'true'
num=[1,4,5,7,1]
print(duplicate(num))
