# 노드 800개
import sys
input = sys.stdin.readline
n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split()) # 거리c는 1000 이하
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향이므로 추가
v1, v2 = map(int, input().rstrip().split())

INF = int(1e9)
distance1 = [INF] * (n+1) # 1 -> min(v1,v2)
distance2 = [INF] * (n+1) # min(v1,v2) -> max(v1,v2)
distance3 = [INF] * (n+1) # max(v1,v2) -> n

import heapq
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1, distance1) # 1->v1 / 1->v2 포함

# case1) 1 -> v1 -> v2 -> n
route1 = distance1[v1]
dijkstra(v1, distance2)
route1 += distance2[v2]
dijkstra(v2, distance3)
route1 += distance3[n]

distance2 = [INF] * (n+1) # 초기화
distance3 = [INF] * (n+1) # 초기화

# case2) 1 -> v2 -> v1 -> n
route2 = distance1[v2]
dijkstra(v2, distance2)
route2 += distance2[v1]
dijkstra(v1, distance3)
route2 += distance3[n]

route = min(route1, route2)
print(route) if 1<=route<INF else print(-1)

# print(f'route1: {route1}')
# print(f'route2: {route2}')
# print(f'dist3: {distance3[n]}')


'''
3% 반례
4 5
1 2 3
1 3 1
1 4 1
2 3 3
3 4 4
2 3
ans: 8

10% 반례
5 4
1 4 1
1 3 1
3 2 1
2 5 1
3 4
ans: 5

25% 반례
4 3
1 2 1
1 3 10
2 4 1
2 3
ans: 22

75% 반례
4 2
1 3 5
2 4 5
3 2
ans: -1
'''