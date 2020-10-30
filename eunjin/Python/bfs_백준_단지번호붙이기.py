from collections import deque

n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited=[[0]*(n) for i in range(n)]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  count = 0

  while queue:
    x,y = queue.popleft()

    if visited[x][y] == 0:
      visited[x][y] = 1
      count += 1
    else:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if visited[nx][ny] == 0 and graph[nx][ny] == 1:
        queue.append((nx,ny))

  return count

post_list =[]
cnt = 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == 0:
      post_list.append(bfs(i,j))


post_list.sort()
print(len(post_list))
for post in post_list :
  print(post)
