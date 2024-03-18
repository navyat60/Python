def palindrome(str):
       for i in range(0,len(str)):
            if(str[i]!=str[len(str)-i-1]):
                return False
       return True
str=input("Enter string:")
if(palindrome(str)==True):
      print("the given string is palindrome")
else:
      print("not a palindrome")