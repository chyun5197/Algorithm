import sys
input = sys.stdin.readline
n = int(input())

d = [0] * (10**6+1) # 2일때부터 인덱스에 값 넣으면 됨

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
print(d[n])
# print(d[1:n+1])