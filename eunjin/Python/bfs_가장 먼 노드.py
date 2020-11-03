from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for a,b in edge:
        adj[a].append(b)
        adj[b].append(a)
    visited = [-1]*(n+1)
    
    return bfs(adj,visited,1)


def bfs(node, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        vertex = queue.popleft()
        for current in node[vertex]:
            if visited[current] == -1:
                queue.append(current)
                visited[current] = visited[vertex] + 1
    result = 0
    value = max(visited)
    for x in visited:
        if x == value:
            result += 1
    return result
