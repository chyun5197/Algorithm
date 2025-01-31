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

depth = [-1] * (n+1)
depth[r] = 0
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            depth[i] = depth[v] + 1
            dfs(graph, i, visited)

visited = [False] * (n+1)
dfs(graph, r, visited)
print(*depth[1:], sep='\n')