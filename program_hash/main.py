import time

class student:
  def __init__(self,student):
    self.Slist = []
    self.Slist.append(student)
    return
  def Turn2String(self):
    return self.Slist[0]

def Findssn(student):
  if type(student) != str:
    student = student.Turn2String()
  elif len(student) == 11:
    return student
  bits = student
  bits = str(bits).split()
  return bits[2]

def Findage(student):
  if type(student) != str:
    student = student.Turn2String()
  bits = student
  bits = str(bits).split()
  return float(bits[4])

def Exists(dictonary,key_looking_for):
  if Findssn(key_looking_for) in dictonary:
    return True
  else:
    return False

def Insert(dictonary,key_to_insert):
  if Exists(dictonary,key_to_insert):
    return False
  else:
    dictonary['size'] = dictonary['size'] + 1
    dictonary[Findssn(key_to_insert)] = key_to_insert
    return

def Traverse(dictonary):
  AA = 0
  for key in dictonary.keys():
    if key == 'size':
      pass
    else:
      AA += Findage(dictonary[key])
  AA = AA/dictonary['size']
  return AA

def Delete(dictonary,key_to_delete):
  if Exists(dictonary,key_to_delete):
    del dictonary[key_to_delete]
    dictonary['size'] = dictonary['size'] - 1
    return
  else:
    print(key_to_delete)
    return False

def Retrieve(dictonary,key_to_find):
  if Exists(dictonary,key_to_find):
    return Findage(dictonary[key_to_find])
  else:
    print(key_to_find)
    return False

def Size(dictonary):
  return dictonary['size']














def main():
  Ttime = time.time()
  StudentList = {'size':0}
  IN = open('InsertNamesM.txt','r')

  #copys names form insertnames into objects and put them into a list
  start = time.time()
  for line in IN:
    Insert(StudentList,line)
  IN.close()
  stop = time.time() - start
  print(stop)
  print('\n')

  start = time.time()
  print(Traverse(StudentList))
  stop = time.time() - start
  print(stop)
  print('\n')

  Del = open('DeleteNamesM.txt','r')
  start = time.time()
  for line in Del:
    line = line.strip()
    Delete(StudentList,line)
  Del.close()
  stop = time.time() - start
  print(stop)
  print('\n')

  Find = open('RetrieveNamesM.txt','r')
  AverageAge = 0
  Size = 0
  start =time.time()
  for line in Find:
    line = line.strip()
    answer = Retrieve(StudentList,line)
    if answer != str:
      AverageAge += Retrieve(StudentList,line)
      Size += 1
  print(AverageAge/Size)
  Find.close()   
  stop = time.time() - start
  print(stop)
  print('\n')
  stop = time.time() - Ttime
  print(stop)
  print('the code is done')

main()
