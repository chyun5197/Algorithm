import sys
input = sys.stdin.readline
n = int(input())
graph = list(map(int, input().split()))
tmp = list(set(graph))
tmp.sort()

k = {}
for i,v in enumerate(tmp):
    k[v] = i
for i in graph:
    if i not in k:
        print(0, end=' ')
    else:
        print(k[i], end=' ')