import sys
input = sys.stdin.readline
n = int(input())
graph = list(map(int, input().split()))
tmp = set(graph)
tmp = list(tmp)
tmp.sort()
for i in range(n):
    ans = tmp.index(graph[i])
    if tmp==-1:
        print(0, end= ' ')
    else:
        print(ans, end=' ')
# print(*nums, sep=' ')

