def check(a,b):
  foot = []
  while a != 0:
    foot.append(a)
    a = a//2
  while b != 0:
    b = b//2
    if b in foot:
      return False
  return True

array = [[1,2],[3,4],[-1,-1],[-1,-1],[-1,-1]]


arr = []
for i in range(0,len(array)):
    arr.append(i)

import itertools

nCr = itertools.combinations(arr, 2)

answer = 0
for a,b in list(nCr):
  if check(a,b):
    print(a,b)
    answer += 1






