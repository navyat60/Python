def AND(a,b):
    if a==1 and b==1:
        return True
    else:
        return False

print(AND(1,1))
print("A=False | B=False A and B="+str(AND(0,0)))
print("A=False | B=True A and B="+str(AND(0,1)))
print("A=True | B=False A and B="+str(AND(1,0)))
print("A=True | B=True A and B="+str(AND(1,1)))

def OR(a,b):
    if a==0 and b==0:
        return False
    else:
        return True

print("OR")
print("A=False | B=False A or B="+str(OR(0,0)))
print("A=False | B=True A or B="+str(OR(0,1)))
print("A=True | B=False A or B="+str(OR(1,0)))
print("A=True | B=True A or B="+str(OR(1,1)))

