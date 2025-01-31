import sys
input = sys.stdin.readline
n,m=map(int,input().rstrip().split())
a = list(map(int,input().split()))
sums = [0]
total = 0
for i in range(n):
    total += a[i]
    sums.append(total)
    # sums.append(sum(a[:i+1]))
for _ in range(m):
    i,j = map(int,input().split())
    print(sums[j]-sums[i-1])