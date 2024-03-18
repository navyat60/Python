l =int(input("Enter the number:")) #900
u = int(input("Enter the end value:"))#1000
print("Prime numbers between", l, "and", u, "are:")
for num in range(l, u + 1):
 # all prime numbers are greater than 1
   if num > 1:
             for i in range(2, num):
                 if (num % i) == 0:
                  break
             else:
                 print(num)
