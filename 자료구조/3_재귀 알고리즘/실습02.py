# 입력한 정수 n에 대하여 1~n까지 출력하는 재귀함수를 만드시오.
# 코드 구현은 각자 다를수도
def f(n):
    if n > 0:
        print(n)
        f(n - 1)


n = int(input())
f(n)

'''
f(3) : print(3) 실행후 f(2)
f(2) : print(2) 실행후 f(1)
f(1) : print(1) 
f(0) : 조건식False

f(1): 
    print(3)
    print(2) 
    print(1)
'''