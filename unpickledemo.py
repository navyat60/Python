import pickle
fp=open("picklefile.txt","rb")
unpickle=pickle.load(fp)
print(unpickle)