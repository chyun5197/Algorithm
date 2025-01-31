'''
아이디어: 뒤에서부터 체크

dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i]+i])
dp[i] = max(p[i] + dp[t[i] + i], max_value)
'''
import sys
input = sys.stdin.readline
n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0] * (n+1)
max_value = 0 # 뒤에서부터 계산할때 현재까지의 최대 상담 금액

# 리스트를 뒤에서부터 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time<=n: # 상담이 기간 안에 끝나는 경우
        dp[i] = max(p[i] + dp[time], max_value) # 현재까지의 최대 이익 계산
        max_value = dp[i]
    else: # 상담이 기간을 벗어나는 경우
        dp[i] = max_value
print(max_value)
