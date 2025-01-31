# 가장 긴 증가하는 부분 수열(Longest Increasing sunbsequence) O(NlogN)
# 해당 원소를 마지막 원소로 가지면서 증가하는 수열 만들기

# 백준) 가장 긴 증가하는 부분 수열(11053)
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]: # j로 순회할때마다 dp[i] 갱신
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))