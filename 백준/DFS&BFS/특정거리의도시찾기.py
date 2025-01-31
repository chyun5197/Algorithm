# 18352번 dfs 실패
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 재귀함수 깊이 늘리기 (원래는 1000까지로 얕음)

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

# city = [[] for i in range(n + 1)] # 거리가 k 되는 도시 체크
city = [0]*(n+1) # 거리가 k 되는 도시 체크
length = -1
def dfs(graph, v):
    global length
    length += 1
    if length>k:
        length-=1
        return
    for i in graph[v]:
        dfs(graph, i)
    if city[v] == 0:
        city[v] = length
    elif length < city[v]:
        city[v] = length
    length -=1

# visted = [False]*(n+1)
dfs(graph, x)
no = True
for i in range(n+1):
    if city[i] == k:
        print(i)
        no = False
if no:
    print(-1)