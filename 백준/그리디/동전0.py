# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

start = n-1
cnt = 0
left = k
while start!=-1:
    if coins[start]>left:
        start -= 1
        continue
    cnt += left//coins[start]
    left %= coins[start]
    start -= 1
    if left == 0:
        break
print(cnt)



