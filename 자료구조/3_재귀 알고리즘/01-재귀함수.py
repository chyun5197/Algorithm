'''
# 재귀(recursion, 순환)
함수가 자기 자신을 다시 호출하여 문제를 해결하는 프로그래밍 기법
재귀 함수 대부분은 반복문으로도 완전탐색 가능
재귀 호출을 멈추는 종료지점이 반드시 있어야 함을 주의!!
    => 없으면 무한루프에 빠짐
'''
# 함수 안에서 다른 함수를 호출할 수 있다.
def hello():
    print("안녕하세요")

def repeat(n):
    for i in range(n):
        hello()
repeat(3)

# 재귀함수) 함수 안에서 본인을 호출할 수 있다.
def fac(num): # 재귀함수로 팩토리얼(n~1곱하기) 완전탐색
    if num==0:
        return 1
    else:
        return num*fac(num-1)
print(fac(5))
# 반복문for Prac06 동일