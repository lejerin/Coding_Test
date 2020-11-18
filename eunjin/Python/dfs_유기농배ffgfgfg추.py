import itertools

def dfs(x,y):
  visited[x][y] = 1
  direction = [(1,0),(-1,0),(0,1),(0,-1)]
  for dx,dy in direction:
    nx = dx + x
    ny = dy + y
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
      continue
    if graph[nx][ny] != 1 and visited[nx][ny] == 0:
      graph[nx][ny] = max(graph[x][y], graph[nx][ny])
      graph[x][y] = max(graph[x][y], graph[nx][ny])
      dfs(nx,ny)

def getSafe(graph):
  for i in range(n):
    for j in range(m):
      if graph[j][i] != 1 and visited[j][i] == 0:
        dfs(j,i)

  result = 0
  for i in range(n):
    for j in range(m):
      if graph[j][i] == 0:
        result += 1

  print(graph)
  return result 

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

#벽 세우기
empty = []
for i in range(n):
  for j in range(m):
    if graph[j][i] == 1:
      empty.append((j,i))


answer = 0

nPr = list(itertools.permutations(empty, 3))
for i in nPr:
  node = graph
  for k in range(3):
    a, b = i[k]
    node[a][b] = 1
  print(i)
  print(graph)
  print(node)
  answer = max(getSafe(node), answer)
    

print(answer)



