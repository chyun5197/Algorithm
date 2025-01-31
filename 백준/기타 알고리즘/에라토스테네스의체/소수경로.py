# 에라토스테네스의 체 알고리즘
# import math
t = int(input())

# 1000~9999
array = [True for i in range(1000, 10000)]  # 모든 수 소수로 초기화
for i in range(2, 100 + 1):
    if array[i]:
        j = 2
        while i * j <= 100:
            array[i * j] = False
            j += 1

for _ in range(t):
    m,n = map(int,input().split())
    print(array[m:n+1].count(True))