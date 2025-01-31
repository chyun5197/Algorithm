# 플로이드
import sys
input = sys.stdin.readline
n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
ans = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(n):
        graph[i+1][j+1] = k[j]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = 1 if graph[a][b] == 1 or graph[a][k] + graph[k][b] == 2 else 0

# print(*graph, sep='\n')
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=' ')
    print()