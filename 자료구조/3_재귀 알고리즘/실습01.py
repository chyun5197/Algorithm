# 시연
# 입력한 정수 n에 대하여 1~n까지 출력하는 재귀함수를 만드시오.
def f(n):
    if n > 1:
        f(n-1)
    print(n)

n = int(input())
f(n)

'''
f(3) : f(2) 실행후 print(3)
f(2) : f(1) 실행후 print(2)
f(1) : 조건식False print(1)

f(3): 
    print(1) 
    print(2) 
    print(3)
'''