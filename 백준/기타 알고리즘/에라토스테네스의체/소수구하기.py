# 에라토스테네스의 체 알고리즘
import math
m,n = map(int,input().split())
array = [True for i in range(n+1)] # 모든 수 소수로 초기화
for i in range(2, int(math.sqrt(n))+1):
    if array[i]:
        j = 2
        while i*j<=n:
            array[i*j] = False
            j += 1
array[1] = False
for i in range(m, n+1): # 모든 소수 출력
    if array[i]:
        print(i)