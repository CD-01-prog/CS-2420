import random
import math
import sys

sys.setrecursionlimit(5500)

def RandomList(A):
  answer = []
  for i in range(A):
    answer.append(random.randrange(A))
  return answer

def NearRandomList(A):
  RL = RandomList(A)
  RL.sort()
  RL[0],RL[A-1] = RL[A-1],RL[0]
  return RL

def bubble(A):
  C = []
  S = []
  switch = True
  while switch:
    switch = False
    for i in range(len(A) - 1):
      if A[i] > A[i + 1]:
        S.append(1)
        C.append(1)
        switch = True
        tempspot = A[i+1]
        A[i+1] = A[i]
        A[i] = tempspot
      C.append(1)
  return math.log(len(S),2)

test_number = 2**3

def main():
  sorts = [bubble]
  for sort in sorts:
    Biglist = NearRandomList(test_number)
    Truelist = []
    for i in Biglist:
      Truelist.append(i)
    Truelist.sort()
    Biglist = sort(Biglist)
    print(Biglist)
main()
