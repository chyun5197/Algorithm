import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

from collections import deque

ords = [0] * (n+1)
count = 0
def bfs(graph, start, visited):
    global count
    visited[start] = True
    q = deque([start])
    while q:
        v = q.popleft()
        count += 1
        ords[v] = count
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

visited = [False] * (n+1)
bfs(graph, r, visited)
for i in range(1, n+1):
    print(ords[i])