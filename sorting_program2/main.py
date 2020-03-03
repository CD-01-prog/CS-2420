import random
def RandomList(A):
  answer = []
  for i in range(A):
    answer.append(random.randrange(A))
  return answer

def mergesort(A):
  if len(A) <= 1:
    return 
  mid = len(A)//2
  L = A[0:mid]
  R = A[mid:]
  mergesort(L)
  mergesort(R)
  i =0
  j =0
  k =0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      A[k] = L[i]
      k+=1
      i+=1
    else:
      A[k] = R[j]
      k+=1
      j+=1
  while i < len(L):
    A[k] = L[i]
    k+=1
    i+=1
  while j < len(R):
    A[k] = R[j]
    k+=1
    j+=1

def quicksortR(A,low,high):
  if high - low <= 0:
    return 
  pivot = low
  lmgt = low +1
  for i in range(low + 1, high +1):
    if A[i]<A[pivot]:
      A[i],A[lmgt]=A[lmgt],A[i]
      lmgt += 1
  pivot = lmgt -1
  A[low],A[pivot] = A[pivot],A[low]
  quicksortR(A,pivot+1,high)
  quicksortR(A,low, pivot-1)

def MquicksortR(A,low,high):
  if high - low <= 0:
    return 
  pivot = len(A)//2
  lmgt = low + 1
  for i in range(low + 1, high + 1):
    if A[i]<A[low]:
      A[i],A[lmgt]=A[lmgt],A[i]
      lmgt += 1
  pivot = lmgt - 1
  A[low],A[pivot] = A[pivot],A[low]
  MquicksortR(A,pivot + 1,high)
  MquicksortR(A,low, pivot - 1)

def countingsort(A):
  F = []
  for i in range(len(A)):
    F.append(0)
  for i in A:
    F[i] += 1
  i = 0
  j = 0
  while i < len(A):
    if F[j] > 0:
      A[i] = j
      i += 1
      F[j] -= 1
    else:
      j += 1

def quicksort(A):
  quicksortR(A,0,len(A)-1)
def Mquicksort(A):
  MquicksortR(A,0,len(A)-1)

def main():
  sorts = [mergesort,quicksort,Mquicksort,countingsort]
  for sort in sorts:
    Biglist = RandomList(6)
    Truelist = []
    for i in Biglist:
      Truelist.append(i)
    Truelist.sort()
    sort(Biglist)
    print(Truelist)
    print(Biglist)
    if Biglist == Truelist:
      print(True)
    else:
      print(False)
    
main()


"""
def quicksort(A):
  if len(A) <= 1:
    return 
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

  
def Mquicksort(A):
  if len(A) <= 1:
    return 
  TL = []
  TM = []
  pivot = A[len(A)//2]
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
"""
