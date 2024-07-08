import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())
mydb=myclient["CMREC"]
mydblist=myclient.list_database_names()
if "CMREC" in mydblist:
    print("database exists")
else:
    print("database doesn't exist")

mycol=mydb["CSE-A"]
mylist=mydb.list_collection_names()
if "CSE-A" in mylist:
    print("exists")
else:
    print("doesn't exists")

mydict={"name":"Navya","rollno":"228r1a0560"}

x=mycol.insert_one(mydict)
