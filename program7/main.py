import time
from UUC import UUC

def main():
  Studentlist = UUC()
  AverageAge = 0

  #insert names into the list
  IN = open('InsertNames.txt','r')
  start = time.time()
  for line in IN:
    Studentlist.insert(line)
  IN.close()
  stop = time.time() - start
  print(stop)
  print(Studentlist.size())

  #find the average age of the list
#  start = time.time()
#  Studentlist.Traverse()
#  AA = AverageAge/Studentlist.size()
#  print(AA)
#  stop = time.time() - start
#  print(stop)

  #delete names from the list
  Del = open('DeleteNames.txt','r')
  start = time.time()
  for line in Del:
    Studentlist.Delete(line.strip())
  Del.close()
  stop = time.time() - start
  print(stop)
  print(Studentlist.size())

  #find average age of select people in the list
#  Find = open('RetrieveNames.txt','r')
#  start =time.time()
#  AverageAge = 0
#  Size = 0
#  for line in Find:
#    found = Studentlist.retrive(line)
#    Size += 1
#  print(AverageAge/Size)
#  Find.close()   
#  stop = time.time() - start
#  print(stop)
  print('the code is done')

main()
