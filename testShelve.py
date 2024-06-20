import shelve
sh=shelve.open("shelve")
print(list(sh.keys()))