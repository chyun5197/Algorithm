'''백준 10870번
피보나치 수 설계하기
f(4) = 3
f(4) = f(3) + f(2)
f(3) = f(2) + f(1)
f(2) = f(1) + f(0)
'''
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n - 1)

num = int(input())
print(fibo(num))

