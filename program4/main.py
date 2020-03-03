import time

class student:

  def __init__(self,student):
    self.Slist = []
    self.Slist.append(student)
    return
  def Turn2String(self):
    return self.Slist[0]

def CheckStudent(potiontal, current):
  for person in current :
    if Findssn(person) == Findssn(potiontal):
      print("someone else has this SSN number error")
      return False
  return True

def Findssn(student):
  if type(student) != str:
    student = student.Turn2String()
  bits = student
  bits = str(bits).split()
  return bits[2]

def main():
  start = time.time()
  StudentList = []
  IN = open('InsertNames.txt','r')
  for line in IN:
    if CheckStudent(line,StudentList):
        NewStudent = student(line)
        StudentList.append(NewStudent)
  IN.close()
  stop = time.time() - start
  print(stop)
  print('the code is done')

main()
