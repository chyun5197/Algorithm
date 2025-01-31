import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
f = [0]*(n+2)
c1, c2 = 0, 0
# def fib(n):
#     global c1
#     if n==1 or n==2:
#         c1 += 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

def fibLoop(n):
    global c2
    f[1] = f[2] = 1
    for i in range(3, n+1):
        c2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fibLoop(n), c2)