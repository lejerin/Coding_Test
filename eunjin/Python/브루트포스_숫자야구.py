from itertools import permutations

def check(num, now, s, b):
  strike = 0
  ball = 0
  for i in range(3):
    if str(num)[i] == str(now[i]):
      strike += 1
    else:
      if str(now[i]) in list(str(num)):
        ball += 1
  if s == strike and b == ball:
    return True
  return False

k = int(input())
answer = list(permutations(range(1,10), 3))


for _ in range(k):
  temp = []
  num, s, b = map(int, input().split())
  for i in answer:
    now_set = set(i)
    if len(list(now_set)) == 3:
        if check(num,i,s,b) == True:
          temp.append(i)
  answer = temp
 
print(len(answer))
