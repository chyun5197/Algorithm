'''
# 다이나믹 프로그래밍
한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘

언제 사용: 1) 최적 부분 구조 탐색 2) 부분 문제들의 중복
탑다운 방식: 큰 문제를 해결하기 위해 작은 문제를 호출. 재귀함수. 메모이제이션 활용
바텀업 방식: 작은 문제부터 차근차근 답을 도출. 반복문.
결과 저장용 DP 테이블 리스트

# 다이나믹 프로그래밍 vs 분할 정복
공통점: 최적 부분 구조를 가질때 사용. 큰 문제를 작은 문제로 나누어 답을 모아서 큰 문제를 해결
차이점
다이나믹은 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
분할 정복은 동일한 부분 문제가 반복적으로 계산되지 않는다.

# 문제 접근 방법
1. 그리디, 완전탐색 등으로 가능한지
2. 안되면 다이나믹 프로그래밍 고려
일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 문제가 출제되는 경우가 많다.
왜냐면 점화식 자체를 떠오르는게 시간이 걸리기 때문
반복 연습 많은 문제 풀어봐야함

대표예제) 백준 123더하기, 계단오르기 등
'''
# 피보나치 탑다운 재귀함수
d = [0] * 100 # 인덱스 1~99로 사용
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0: # 이미 계산한 적이 있으면 그대로 반환
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# 피보나치 바텀업 반복문
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[99])

# 개미 전사
n = int(input())
arr = list(map(int, input().split()))
d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])
print(d[n-1])


