import random
import math

def RandomList(A):
  answer = []
  for i in range(A):
    answer.append(random.randrange(A))
  return answer

def mergesort(A):
  compares = []
  swaps = []
  if len(A) <= 1:
    compares.append(1)
    return 
  compares.append(1)
  mid = len(A)//2
  L = A[0:mid]
  R = A[mid:]
  swaps.append(1)
  mergesort(L)
  swaps.append(1)
  mergesort(R)
  i =0
  j =0
  k =0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      compares.append(1)
      swaps.append(1)
      A[k] = L[i]
      k+=1
      i+=1
    else:
      A[k] = R[j]
      compares.append(1)
      swaps.append(1)
      k+=1
      j+=1
  while i < len(L):
    A[k] = L[i]
    swaps.append(1)
    k+=1
    i+=1
  while j < len(R):
    A[k] = R[j]
    swaps.append(1)
    k+=1
    j+=1
  return math.log(len(swaps),2)

def quicksort(A):
  if len(A) <= 1:
    return A
  TL = []
  TM = []
  pivot = A[0]
  TR = []
  for num in A:
    if num < pivot:
      TL.append(num)
    elif num == pivot:
      TM.append(num)
    else:
      TR.append(num)
  TL = quicksort(TL)
  TR = quicksort(TR)
  for num in range(len(TM)):
    TL.append(TM[num])
  for num in range(len(TR)):
    TL.append(TR[num])
  A = TL
  return A
  
def Mquicksort(A):
  C = []
  S = []
  if len(A) <= 1:
    C.append(1)
    return A
  C.append(1)
  TL = []
  TM = []
  pivot = A[len(A)//2]
  TR = []
  for num in A:
    if num < pivot:
      C.append(1)
      TL.append(num)
    elif num == pivot:
      C.append(1)
      TM.append(num)
    else:
      C.append(1)
      TR.append(num)
  TL = quicksort(TL)
  TR = quicksort(TR)
  for num in range(len(TM)):
    TL.append(TM[num])
  for num in range(len(TR)):
    TL.append(TR[num])
  A = TL
  print(len(C))
  return A


def countingsort(A):
  C = []
  S = []
  F = []
  for i in range(len(A)):
    F.append(0)
  for i in A:
    F[i] += 1
  i = 0
  j = 0
  while i < len(A):
    C.append(1)
    if F[j] > 0:
      C.append(1)
      A[i] = j
      S.append(1)
      i += 1
      F[j] -= 1
    else:
      C.append(1)
      j += 1
  print(len(S))
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
  sorts = [mergesort]
  for sort in sorts:
    Biglist = RandomList(8)
    Truelist = []
    for i in Biglist:
      Truelist.append(i)
    Truelist.sort()
    Biglist = sort(Biglist)
    print(Biglist)
    
    

for i in range(100):
  main()
