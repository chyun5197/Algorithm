# 무방향 그래프, 간선 트리, 서로소 집합
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n+1)] # 부모테이블

def findParent(x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m): # 입력 받으면서 바로 합집합 수행
    u, v = map(int, input().split())
    unionParent(u, v)

components = set()
for i in range(1, n+1): # 각 원소가 속한 루트노드 집합에 추가
    components.add(findParent(i))
print(len(components))
