# 최소 스패닝 트리
# 모든 두 노드 사이 거리를 확인하면 메모리 초과나옴
import sys
input = sys.stdin.readline
n = int(input())
parent = [i for i in range(n+1)] # 부모테이블
edges = []
result = 0

x, y, z = [], [], []
for i in range(1, n+1):
    node = tuple(map(int,input().split()))
    x.append((node[0], i)) # (위치, 노드번호)
    y.append((node[1], i))
    z.append((node[2], i))

# 인접한 위치의 노드끼리 연산을 위해 정렬
x.sort()
y.sort()
z.sort()

# x,y,z 이동 방향 상관없이(무방향 그래프) 모두 edges에 추가
# 추후 최소비용 (n-1)개의 간선만 연결하고 비용 후순위 간선은 연산에서 제외
for i in range(n-1): # O(3n)
    # cost a b
    # x,y,z 전부 하나에 삽입
    edges.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    edges.append((abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))

# 아래방법 메모리초과: 탐색할 간선 경우를 줄여야함 <= O(n^2)
# for i in range(1, n+1): # n^2/2번 수행
#     for j in range(i+1, n+1):
#         cost = min(abs(nodes[i][0]-nodes[j][0]),
#                    abs(nodes[i][1]-nodes[j][1]),
#                    abs(nodes[i][2]-nodes[j][2]))
#         # edges.append((cost, i, j))
#         heapq.heappush(edges, (cost, i, j))

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort() # 간선을 비용순 정렬
# finalEdges = []
for edge in edges:
    cost, i, j = edge
    if findParent(parent, i) != findParent(parent, j):
        unionParent(parent, i, j)
        result += cost
        # finalEdges.append(edge)
print(result)
# print(finalEdges)






