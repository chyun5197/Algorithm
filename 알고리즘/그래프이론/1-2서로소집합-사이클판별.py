'''
# 사이클이란?
그래프의 특정 노드에서 출발하여 돌아다니다가 다시 처음 출발했던 곳으로 되돌아 갈 수 있는 경우

# 서로소 집합을 활용한 사이클 판별
서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용 가능 (사이클 여부는 DFS로 판별)

# 사이클 판별 알고리즘
1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
    1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union) 연산 수행
    2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복
'''
# 특정 원소가 속한 집합을 찾기
def findParent(x): # (부모테이블, 노드번호) | 함수명은 통상적으로 왼쪽처럼 지음
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return findParent(parent[x])
    # return x
    return parent[x] # 경로 압축: find 함수를 재귀 호출한 뒤에 '부모 테이블 값을 바로 갱신'한다.

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
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#============ 여기서부터 다름 =============#
cycle = False # 사이클 발생 여부
for i in range(e):
    a, b = map(int, input().split())
    if findParent(a) == findParent(b): # 사이클이 발생한 경우 종료
        cycle = True
        break
    else: # 사이클이 발생하지 않았다면 union 연산 수행
        unionParent(a, b)

print('사이클 발생') if cycle else print('사이클 미발생')
