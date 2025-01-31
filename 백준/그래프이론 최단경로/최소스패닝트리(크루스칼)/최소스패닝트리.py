import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [i for i in range(v+1)] # 부모테이블 자기 자신으로 초기화

# 특정 원소가 속한 집합을 찾기
# def findParent(parent, x): # (부모테이블, 노드번호) | 함수명은 통상적으로 왼쪽처럼 지음
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
#     if parent[x] != x:
#         return findParent(parent, parent[x])
#     return parent[x]

def findParent(x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def unionParent(a, b):
    # a = findParent(parent, a)
    # b = findParent(parent, b)
    a = findParent(a)
    b = findParent(b)
    if a < b: # 번호가 더 큰 쪽이 작은쪽을 부모로 설정
        parent[b] = a
    else:
        parent[a] = b
edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용
for _ in range(e): # 모든 간선에 대한 정보 입력 받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순 정렬위해 cost를 0번으로 설정
edges.sort() # 간선을 비용순으로 정렬

connect = 0 # 연결된 간선 개수 체크
for edge in edges: # 모든 간선 확인하여 사이클 아닌 경우에만 합집합(집합에 포함)
    cost, a, b = edge
    # if findParent(parent, a) != findParent(parent, b):
    if findParent(a) != findParent(b):
        unionParent(a, b)
        result += cost
print(result)