import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

share = n//5
for i in range(share, -1, -1):
    left = n-i*5
    if left % 3 == 0:
        cnt = i + left//3
        break
print(cnt) if cnt else print(-1)
