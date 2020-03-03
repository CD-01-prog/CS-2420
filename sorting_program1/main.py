import random
def RandomList(size):
  A = []
  for i in range(size):
    A.append(random.randrange(size))
  return A

def bubble(A):
  switch = True
  while switch:
    switch = False
    for i in range(len(A) - 1):
      if A[i] > A[i + 1]:
        switch = True
        tempspot = A[i+1]
        A[i+1] = A[i]
        A[i] = tempspot

def shaker(A):
  switch = True
  while switch:
    switch = False
    for i in range(len(A) - 1):
      if A[i] > A[i + 1]:
        switch = True
        A[i],A[i+1] = A[i + 1],A[i]
    for i in range(len(A)-2, -1, -1):
      if A[i + 1] < A[i]:
        switch = True
        A[i],A[i+1] = A[i + 1],A[i]

def selection(A):
  smallestspot = 0
  smallestnumber = 0
  for i in range(len(A)-1):
    smallestspot = i
    smallestnumber = A[i]
    for num in range(i,len(A)):
      if A[num] < smallestnumber:
        smallestnumber = A[num]
        smallestspot = num
    if i != smallestspot:
      tempnumber = A[i]
      A[i] = A[smallestspot]
      A[smallestspot] = tempnumber
  
def main():
  Biglist = RandomList(10)
  Truelist = []
  for i in Biglist:
    Truelist.append(i)
  Truelist.sort()
  bubble(Biglist)
  if Biglist != Truelist:
    return print('error bubble')
  print(Truelist)
  print(Biglist)

  Biglist = RandomList(10)
  Truelist = []
  for i in Biglist:
    Truelist.append(i)
  Truelist.sort()
  shaker(Biglist)
  if Biglist != Truelist:
    return print('error shaker')
  print(Truelist)
  print(Biglist)

  Biglist = RandomList(10)
  Truelist = []
  for i in Biglist:
    Truelist.append(i)
  Truelist.sort()
  selection(Biglist)
  if Biglist != Truelist:
    return print('error selection')
  print(Truelist)
  print(Biglist)
main()
