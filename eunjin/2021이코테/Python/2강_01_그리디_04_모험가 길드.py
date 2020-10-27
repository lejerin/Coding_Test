#모험가 길드

#x가 적은 것 끼리만 모아두기

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
