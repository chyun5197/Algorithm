import sys
input = sys.stdin.readline
n = int(input())
k = list(map(int, input().split()))

dp = [1] * n
# print(k)
for i in range(1, n):
    for j in range(0, i):
        if k[j] > k[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
print(n-max(dp))

