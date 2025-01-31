import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    a, b = map(int, input().split())
    graph.append((a,b))
graph.sort(key=lambda x:[x[0], x[1]])
for i in graph:
    print(i[0], i[1])