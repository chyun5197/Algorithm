n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
# print(graph)


def dfs(graph, v, visited): # DFS
    visted[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque # BFS
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visted = [False]*(n+1)
dfs(graph, v, visted)
print()
visted = [False]*(n+1)
bfs(graph, v, visted)
