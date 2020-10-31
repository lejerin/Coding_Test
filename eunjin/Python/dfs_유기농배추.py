# 유기농 배추
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


list = []
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1
                
    list.append(result)

for i in range(len(list)):
  print(list[i])



  



