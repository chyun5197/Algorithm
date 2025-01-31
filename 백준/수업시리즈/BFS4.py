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

depth = [-1] * (n+1)
ords = [0] * (n+1)
order = 0
def bfs(graph, start, visited):
    global order
    visited[start] = True
    depth[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        order += 1
        ords[v] = order
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                depth[i] = depth[v] + 1
                q.append(i)

visited = [False] * (n+1)
bfs(graph, r, visited)
t = 0
for i in range(1,n+1):
    t += depth[i]*ords[i]
print(t)