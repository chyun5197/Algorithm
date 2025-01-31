'''
# 신장 트리(스패닝 트리, Spanning Tree)
그래프에서 모든 노드를 잇지만 사이클이 존재하지 않는 부분 그래프
(모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도함)

# 최소 신장 트리(MST)
최소한의 비용으로 구성되는 신장 트리를 찾아야할 때
간선의 가중치 합이 최소가 되는 신장 트리

# 크루스칼 알고리즘
- 최소 신장 트리 알고리즘
- 그리디 알고리즘
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함O
    2) 사이클이 발생하는 경우 최소 신장 트리에 포함X
3. 모든 간선에 대해 2번 과정 반복

# 크루스칼 알고리즘 성능
- 간선 개수 E개 일때 O(ElogE)
- 알고리즘에서 가장 많은 시간 요구는 간선 E개를 정렬할때임
'''
# # 특정 원소가 속한 집합을 찾기
# def findParent(parent, x): # (부모테이블, 노드번호) | 함수명은 통상적으로 왼쪽처럼 지음
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
#     if parent[x] != x:
#         return findParent(parent, parent[x])
#     return parent[x]
#
# # 두 원소가 속한 집합을 합치기
# def unionParent(parent, a, b):
#     a = findParent(parent, a)
#     b = findParent(parent, b)
#     if a < b: # 번호가 더 큰 쪽이 작은쪽을 부모로 설정
#         parent[b] = a
#     else:
#         parent[a] = b
def findParent(x):
    if parent[x] == x:
        return x
    return findParent(parent[x])

# 두 원소가 속한 집합을 합치기
def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b: # 번호가 더 큰 쪽이 작은쪽을 부모로 설정
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())

# parent = [0] * (v+1) # 부모 테이블 초기화하기
# for i in range(1, v+1): # 부모 테이블 상에서 부모를 자기 자신으로 초기화
#     parent[i] = i
parent = [i for i in range(v+1)] # 부모테이블 자기 자신으로 초기화

#== 위까지 동일 ==#

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용
for _ in range(e): # 모든 간선에 대한 정보 입력 받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순 정렬위해 cost를 0번으로 설정

edges.sort() # 간선을 비용순으로 정렬

for edge in edges: # 모든 간선 확인하여 사이클 아닌 경우에만 합집합(집합에 포함)
    cost, a, b = edge
    if findParent(a) != findParent(b):
        unionParent(a, b)
        result += cost
    # if findParent(parent, a) != findParent(parent, b):
    #     unionParent(parent, a, b)
    #     result += cost
print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''