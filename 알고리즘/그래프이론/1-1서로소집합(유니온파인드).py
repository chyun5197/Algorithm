'''
# 서로 집합(Disjoint Sets / union-find)
- union 합집합
- find 찾기
- 트리 자료구조 이용

# 문제점
합집합(union) 연산이 편향되게 이루어지는 경우 찾기(find) 함수가 비효율적으로 동작
최악의 경우에는 find 함수가 모든 노드를 다 확인하게 되어 시간 복잡도 O(V)가 된다
=> 경로 압축 기법으로 해결 : return parent[x]
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
    if a < b: # 번호가 더 큰 쪽이 작은쪽을 부모로 설정 (부모를 최상위 루트노드로 설정하는건 아님)
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    unionParent(a, b)

# 각 원소가 속한 집합(최상위 루트노드) 출력하기
print('각 원소가 속한 집합:', end=' ')
for i in range(1, v+1):
    print(findParent(i), end=' ')
print()

# 부모 테이블 내용 출력하기
print('부모 테이블:', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()
'''
입력 예시
6 4
1 4
2 3
2 4
5 6

기본코드
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5 

경로 압축 이후
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5 
'''