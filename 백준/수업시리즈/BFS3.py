import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

ords = [-1] * (n+1)
def bfs(graph, start, visited):
    visited[start] = True
    ords[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                ords[i] = ords[v] + 1
                q.append(i)

visited = [False] * (n+1)
bfs(graph, r, visited)
print(*ords[1:], sep='\n')