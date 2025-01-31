import sys
input = sys.stdin.readline
t = int(input())
test = [int(input()) for _ in range(t)]

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = dp[i - 1]%1000000009 + dp[i - 2]%1000000009 + dp[i - 3]%1000000009

for i in test:
    print(dp[i]%1000000009)