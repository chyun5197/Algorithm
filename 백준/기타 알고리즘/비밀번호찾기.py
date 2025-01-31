import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = {}
for _ in range(n):
    a, b = input().split()
    k[a] = b
for _ in range(m):
    print(k[input().rstrip('\n')])