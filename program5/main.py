import time

class student:

  def __init__(self,student):
    self.Slist = []
    self.Slist.append(student)
    return
  def Turn2String(self):
    return self.Slist[0]

def CheckStudent(line, StudentList):
  for person in StudentList :
    if Findssn(person) == Findssn(line):
      print("someone else has this SSN number error")
      return False
  return True

def HuntAndKill(line, StudentList):
  for person in StudentList :
    if Findssn(person) == line:
      StudentList.remove(person)
      return
  print(line)

def FindStudent(line, StudentList):
  for person in StudentList :
    if Findssn(person) == line:
      return Findage(person)
  print(line)
  return 0

def Findssn(student):
  if type(student) != str:
    student = student.Turn2String()
  bits = student
  bits = str(bits).split()
  return bits[2]

def Findage(student):
  if type(student) != str:
    student = student.Turn2String()
  bits = student
  bits = str(bits).split()
  return float(bits[4])
  

def main():
  StudentList = []
  AverageAge = 0
  IN = open('InsertNames.txt','r')

  #copys names form insertnames into objects and put them into a list
  start = time.time()
  for line in IN:
    if CheckStudent(line,StudentList):
        NewStudent = student(line)
        StudentList.append(NewStudent)
  IN.close()
  stop = time.time() - start
  print(stop)

  #goes over the list and collects their total age then finds and prints the average of that
  start = time.time()
  for line in StudentList:
    AverageAge += Findage(line)
  AA = AverageAge/len(StudentList)
  print(AA)
  stop = time.time() - start
  print(stop)

  #using the ssn numbers from deletenames.txt it removes all those people from the python list and then prints any ssn from deletenames that were not found
  Del = open('DeleteNames.txt','r')
  start = time.time()
  for line in Del:
    line = line.strip()
    HuntAndKill(line,StudentList)
  Del.close()
  stop = time.time() - start
  print(stop)

  #this goes through the student list looking for specific students when found it gets the students age so that the average can be found it prints the ssn of any studetns that were not found
  Find = open('RetrieveNames.txt','r')
  start =time.time()
  AverageAge = 0
  Size = 0
  for line in Find:
    line = line.strip()
    AverageAge += FindStudent(line,StudentList)
    Size += 1
  print(AverageAge/Size)
  Find.close()   
  stop = time.time() - start
  print(stop)
  print('the code is done')

main()
