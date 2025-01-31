# DFS(Depth-First Search, 깊이 우선 탐색) : 멀리(더 깊이) 있는 노드부터 탐색 [스택]
# 137pg 상황
def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end = ' ')
    for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 2차원 리스트 자료형으로 표현
graph = [
    [],
    [2,3,8], # 노드1 연결 : [노드2, 노드3, 노드8]
    [1,7],   # 노드2 연결 : [노드1, 노드7]
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] # 노드8
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 실행
dfs(graph, 1 , visited)
print()
#######################################
# BFS(Breadth First Search, 너비 우선 탐색) : 가까운 노드부터 탐색 [큐]
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 구현을 위해 deque 라이브러리 사용

    visited[start] = True # 현재 노드를 방문 처리
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 실행
bfs(graph, 1 , visited)

