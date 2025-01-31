# 18352번 bfs
'''
7 6 2 1
1 2
1 3
2 4
2 5
3 6
3 7

4
5
6
7
'''
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

from collections import deque
city = []
que = deque([x])
distance = [-1 for i in range(n+1)]
distance[x] = 0
while que:
    now = que.popleft()
    for nextNode in graph[now]:
        if distance[nextNode] == -1:
            distance[nextNode] = distance[now] + 1
            que.append(nextNode)

# print(distance)
no = True
for i in range(n+1):
    if distance[i] == k:
        print(i)
        no = False
if no :
    print(-1)
