import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    if dp[n]!=0:
        return dp[n]
    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]

t = int(input())
test = [int(input()) for i in range(t)]
dp = [0] * 41
dp[0] = 0
dp[1] = 1
fibo(40)

for i in test:
    if i == 0:
        print(1, 0)
        continue
    print(dp[i-1], dp[i])