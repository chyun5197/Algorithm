import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    graph.append((a,b,i))
graph.sort(key=lambda x:[x[0], x[2]])
for i in graph:
    print(i[0], i[1])