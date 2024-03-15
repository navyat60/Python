"""
open()
read()
readline()
write()
writeline()
close()
seek()
tell()
"""
fp1=open("CSEa1.txt","w")
if fp1:
    print("file is created successfully")
fp1.writelines("welcome to cmr engineerng college\nthis is CSE-A\nlet's discuss python")

fp1.close()