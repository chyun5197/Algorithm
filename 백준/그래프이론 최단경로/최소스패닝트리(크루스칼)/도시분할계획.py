# 최소 스패닝으로 간선 제거. 2개의 부분 그래프 집합으로 나눠야함
# 최소 간선으로 만든 후 -> 유지비용 최대인 간선 제거해서 2개 마을로 나누기
import sys
input = sys.stdin.readline

# 노드, 간선
n, m = map(int, input().split())
parent = [i for i in range(n+1)] # 부모테이블 자기 자신으로 초기화
edges = []
result = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

def findParent(parent: object, x: object) -> object:
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

finalEdges = [] # 최종으로 사용될 간선
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
        finalEdges.append(edge)
finalEdges.sort(reverse=True) # 유지비용 최대인 간선 찾고자
print(result - finalEdges[0][0])










