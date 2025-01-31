'''
# 위상 정렬(Topology Sort)
사이클이 없는 방향 그래프(DAG)의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열"하는 것을 의미
방향성에 거스리지 않도록 = 순차적으로
- 진입차수(Indegree) : 특정한 노드로 들어오는 간선의 개수
- 진출차수(Outdegree): 특정한 노드에서 나가는 간선의 개수

# 위상 정렬 알고리즘 (DFS or Queue)
큐를 이용하면
1. 진입차수가 0인 모든 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복
    1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다. (간선 제거해서 다음 노드들의 진입차수를 0으로 만드는것)
    2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
=> 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같아진다.

# 위상 정렬 특징
- 위상 정렬은 DAG(Direct Acyclic Graph, 순환하지 않는 방향 그래프)에 대해서만 수행 가능
- 위상 정렬에서는 여러가지 답이 존재 가능
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다는것
    사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못하기 때문(진입차수 0만 큐 삽입)
- 스택을 활용한 DFS로도 구현 가능

# 성능
위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거해야 한다
-> O(V+E)
'''
from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
indegree = [0] * (v+1) # 모든 노드 진입차수 0으로 초기화
graph = [[] for i in range(v+1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A->B 로 이동 가능
    indegree[b] += 1

print(indegree)
print(graph)

# 위상 정렬 함수
def topologySort():
    result = [] # 알고리즘 수행 결과
    q = deque()
    for i in range(1, v+1): # 진입차수 0인 노드만 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]: # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')
topologySort()
'''
입력 
7 8
1 2 
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''



