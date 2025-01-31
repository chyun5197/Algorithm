import sys
input = sys.stdin.readline
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 최단경로로 가는 도시 경로 추가
detail = [[[i] for _ in range(n+1)] for i in range(n+1)]

for _ in range(m): # 입력
    a, b, c = map(int, input().split())
    if graph[a][b] > c: # 조건: 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
        graph[a][b] = c
        detail[a][b] = [a,b]

for a in range(1, n+1): # \ 0 초기화 작업
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0


import copy
for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

                # 도시 경로도 추가
                tmp = copy.deepcopy(detail[k][b])
                for e in detail[a][k]: # 앞의 경로와 겹치는 도시는 제거
                    if e in tmp:
                        tmp.remove(e)
                detail[a][b] = detail[a][k] + tmp

# 문제 조건: 거리 100000 이상일때는 못감 -> 거리 0 나오게끔, 경로도 안나오게
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] > 100000:
            graph[a][b] = INF
            detail[a][b] = []

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a==b:
            print(0, end=' ')
        else:
            print(len(detail[a][b]), end=' ')
            # print(f'({a},{b}):', end=' ')
            # print(detail[a][b], end=' ')
            for k in detail[a][b]:
                print(k, end=' ')
        print()