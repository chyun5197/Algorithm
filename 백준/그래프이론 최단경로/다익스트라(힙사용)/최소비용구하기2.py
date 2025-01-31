# 노드 1000개니까 힙 활용
# 2에서 추가된건 경로에 포함되는 도시개수, "도시경로"
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
cities = [[] for _ in range(n+1)] # 도시 경로 테이블
# print(*graph, sep='\n')
'''graph[출발노드:(도착노드,거리)]
[]
[(2, 2), (3, 3), (4, 1), (5, 10)]
[(4, 2)]
[(4, 1), (5, 1)]
[(5, 3)]
[]
'''
import heapq
def dijkstrat(start):
    q = []
    heapq.heappush(q, (0, start)) # 힙은 (거리, 도시)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # print(f'\n<pop(거리, 현재도시): ({dist}, {now})>')
        if distance[now] < dist:
            continue
        for i in graph[now]: # graph는 (도시, 거리)
            # print(f'i(도시, 거리): {i}')
            # cities[i[0]].append(now)
            cost = dist+i[1]
            if cost < distance[i[0]]:
                # print(f'{i[0]}도시 가는 더 짧은 거리: {cost}')
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

                # 도시경로를 [현재도시까지 오는동안의 최소도시경로 + 현재도시]로 갱신
                cities[i[0]] = cities[now] + [now]

                # cities[i[0]].append(now)
                # print(f'<push(거리, 도시): ({cost}, {i[0]})>')
        # print('q:', q)
        # print('cities:', cities)
dijkstrat(start)
# print('도시 경로:', cities)
# print('distance:', distance)
print(distance[end])
print(len(cities[end])+1)
# print(start, end=' ')
print(*cities[end], end=' ')
print(end)
'''
예제 case
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

Answer:
4
3
1 3 5 or 1 4 5

Test Case 1
10
2
6 10 11
1 6 7
1 10
    
Answer:
18
3
1 6 10

Output
18
4
1 6 1 0
    
    
    
Test Case 2
21
19
11 14 2
13 11 3
13 19 5
14 16 3
16 17 12
12 20 1
20 18 13
15 11 2
18 16 19
13 17 5
16 12 4
18 19 12
13 19 8
18 21 4
12 17 14
12 14 24
12 13 3
18 13 4
15 20 5
11 21

Answer:
27
7
11 14 16 12 20 18 21

Output:
27
14
1 1 1 4 1 6 1 2 2 0 1 8 2 1
'''