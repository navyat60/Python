try:
  raise IndexError
except IndexError:
  pass
l = [1,2,3]
try:
  l[4]
except IndexError:
  print ("an index error!")