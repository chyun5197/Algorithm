# 소수 판별
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
print(isPrime(4))
print(isPrime(7))

'''
# 에라토스테네스의 체 알고리즘
여러개의 수가 소수인지 아닌지 판별
1) 2부터 N까지의 모든 자연수를 나열
2) 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
3) 남은 수 중에서 i의 배수를 모두 제거
4) 더이상 반복할 수 없을 때까지 2)3) 과정을 반복
'''
n = 1000 # 2~1000까지 판별
array = [True for i in range(n+1)] # 모든 수 소수로 초기화
for i in range(2, int(math.sqrt(n))+1): # 에라토스테네스의 체 알고리즘
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i*j<=n:
            array[i*j] = False
            j += 1
for i in range(2, n+1): # 모든 소수 출력
    if array[i] == True:
        print(i, end=" ")