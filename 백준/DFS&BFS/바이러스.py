n = int(input()) # 컴퓨터 수
m = int(input()) # 간선 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
# print(graph)

virus = [False] * (n+1)
def dfs(graph, v, virus):
    virus[v] = True
    for i in graph[v]:
        if not virus[i]:
            dfs(graph, i ,virus)
dfs(graph, 1, virus)
print(virus.count(True)-1)
