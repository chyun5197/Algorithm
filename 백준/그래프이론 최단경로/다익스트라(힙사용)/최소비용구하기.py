# 노드 1000개니까 힙 활용
import sys
input = sys.stdin.readline
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a->b 거리가 c
start, end = map(int, input().split())

distance = [INF] * (n+1) # 최단 거리 테이블
# print(graph)
# [[], [(2, 2), (3, 3), (4, 1), (5, 10)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []]

import heapq
def dijkstrat(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 힙은 (거리, 도시)
            continue
        for i in graph[now]: # graph는 (도시, 거리)
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstrat(start)
print(distance[end])