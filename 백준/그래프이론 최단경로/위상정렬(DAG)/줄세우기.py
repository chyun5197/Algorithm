import sys
input = sys.stdin.readline
n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
from collections import deque
def topologySort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
topologySort()
for i in result:
    print(i, end=' ')