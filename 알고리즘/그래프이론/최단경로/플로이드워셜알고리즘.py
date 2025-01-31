'''
# 플로이드 워셜 알고리즘
모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
- 다익스트라와 마찬가지로 단계별로 거처 가는 노드를 기준으로 알고리즘을 수행
- 2차원 테이블에 최단 거리 정보를 저장
- 다이나믹 프로그래밍 유형에 속함 (삼중 반복문)
- 노드의 개수가 적을때(500개 이하)에서 유용 ~ 시간복잡도 O(N^3)
- 노드가 많아지면 다익스트라로

다익스트라는 그리디 알고리즘
플로이드는 다이나믹 프로그래밍
'''
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 본인끼리 가는 비용은 0으로 초기화(대각선\)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 값을 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c # a번 노드에서 b번 노드로 가는 비용(거리)이 c이다.

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()