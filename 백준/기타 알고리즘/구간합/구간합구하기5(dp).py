# 사각형 합 / x행y열
import sys
input = sys.stdin.readline
n,m=map(int,input().rstrip().split())
a = [list(map(int,input().split())) for _ in range(n)]
# print(a)

sums = [[0] for _ in range(n)]
total = 0
for i in range(n):
    for j in range(n):
        total += a[i][j]
        sums[i].append(total)
        if i<n-1 and j==n-1:
            sums[i+1][0] = total

# print(*sums, sep='\n')

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().rstrip().split())
    t = 0
    for x in range(x1-1, x2):
        t += sums[x][y2]-sums[x][y1-1]
        # if _ == m-1:
        #     print(t)
    print(t)
