#그래프 탐색 알고리즘: DFS/BFS

#스택 구현
stack = []

stack.append(5)
stack.append(3)
stack.pop()
stack.append(2)

print(stack[::-1]) #최상단 원소부터
print(stack) #최하단 원소부터

#큐 구현
from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.popleft()
queue.append(2)

print(queue) #먼저 들어온 순서대로
queue.reverse()
print(queue) #나중에 들어온 원소부터 


#재귀함수: 자기 자신을 다시 호출하는 함수(종료조건 명시해야함)


#팩토리얼 구현

#반복적
def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

#재귀적
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_iterative(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))

#유클리드 호제법: 최대 공약수 계산

def gcd(a,b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)

print(gcd(192,162))

#DFS 구현
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end= ' ')
  #재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
[], #0은 사용하지 않음
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)

#BFS : 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색/ 큐 자료구조 이용

#BFS 구현
# from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])

  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * 9

print("\nbfs")
bfs(graph, 1, visited)
  
