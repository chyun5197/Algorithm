import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    k = input().split()
    k[1:4] = list(map(int, k[1:4]))
    s.append(k)

s.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in s:
    print(i[0])