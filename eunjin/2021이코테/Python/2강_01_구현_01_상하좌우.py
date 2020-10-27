#구현: 시뮬레이션과 완전 탐색
#머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
#풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제들

#상하좌우 

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

x = 1
y = 1
n = int(input())
plans = input().split()

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if  nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x,y)
