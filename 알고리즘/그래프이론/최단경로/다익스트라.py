''' ==> 백준 최소비용구하기2에서 지나는 경로 확인 자세함
# 다익스트라 알고리즘
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3번과 4번을 반복한다.

방법1
- 총 O(V)에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색한다
- 전체 시간 복잡도는 O(V^2)
- 방법1: 노드 개수가 5000개 이하라면 간단한 코드로 문제 해결
- 방법2: 10000개 이상이면 우선순위 큐 도입

방법2 개선된 구현
- 시간복잡도 O(ElogV)
- 반복문은 노드의 개수(V) 이상의 횟수로는 처리되지 않음
- 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 최대 간선의 개수(E)만큼 연산이 수행
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수 입력
start = int(input())
graph = [[] for _ in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n + 1) # 방문 여부 => 2)에서는 불필요
distance = [INF] * (n + 1) # 최단 거리 테이블

# 모든 간선 정보를 입력
for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용(거리)이 c이다.
    graph[a].append((b, c))

# 1) 기존
# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 리턴
# def getSmallestNode():
#     minValue = INF
#     index = 0 # 가장 최단 거리가 짧은 노드(인덱스 번호로 세팅)
#     for i in range(1, n+1):
#         if distance[i] < minValue and not visited[i]:
#             minValue = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0 # 시작 노드에 대해서 초기화
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1] # graph에 [(b,c),..]로 들어있으니 b번 노드로 이동하는 비용 c로 세팅
#     for i in range(n-1): # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#         now = getSmallestNode() # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
#         visited[now] = True
#         for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
#             cost = distance[now] + j[1]
#             if cost<distance[j]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#                 distance[j] = cost # 거리 대체

# 2) 우선순위큐
import heapq
def dijkstra(start):
    q = [] # [(dist, now),..] (거리,노드번호). now는 현재 꺼낸 노드에 대한 정보 (현재 위치의 노드)

    # 힙 넣을때 거리를 0번에 넣어야 빼낼때 최소 거리순으로 가져온다
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입 | heap은 (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (현재까지 오는데 소요된 거리, 현재 위치의 노드)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: # 테이블에기록된노드까지의거리 < 현재확인하는노드까지의거리
            continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인 | graph[0],[1] = (다음 이동할(인접한) 노드, 거리)
            cost = dist + i[1] # 총거리 = 현재확인하는노드까지의거리 + 인접한노드와의거리(c)
            if cost<distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 (테이블의 기록된 거리와 비교)
                distance[i[0]] = cost # 현재 cost로 갱신
                heapq.heappush(q, (cost, i[0])) # (다음노드까지의 거리, 다음노드)

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF: # 도달할 수 없는 경우
        print("INFINITY")
    else:
        print(distance[i])
