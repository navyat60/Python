def comm(x):
    return x.replace('',',')[1:-1]

x=str(input())
print(repr(comm(x)))