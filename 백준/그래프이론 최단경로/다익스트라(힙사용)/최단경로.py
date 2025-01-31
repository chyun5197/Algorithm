# 노드 20000개니까 힙 활용
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, input().split()) # 거리c는 10 이하
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (v+1)

import heapq
def dijsktra(start):
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
dijsktra(start)
# print(distance[1:], sep='\n')
for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)

