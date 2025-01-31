import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: # 인접정점 오름차순 정렬
    i.sort(reverse=True)

ords = [0] * (n+1)
count = 0

def dfs(graph, v, visited):
    global count
    visited[v] = True
    count += 1
    ords[v] = count
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n+1)
dfs(graph, r, visited)
for i in range(1, n+1):
    print(ords[i])