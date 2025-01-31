import sys
input = sys.stdin.readline
n = int(input())
s = [0] + [int(input()) for _ in range(n)]
a = [{} for i in range(n+1)]

if n==1:
    print(s[1])
elif n==2:
    print(s[1]+s[2])
elif n==3:
    print(max(s[1], s[2]) + s[3])
else:
    a[1][1] = s[1]
    a[2][1] = s[2]
    a[2][2] = s[1] + s[2]
    a[3][1] = a[1][1] + s[3]
    a[3][2] = a[2][1] + s[3]

    for i in range(4, n+1):
        a[i][1] = max(a[i-2][1], a[i-2][2]) + s[i]
        a[i][2] = a[i-1][1] + s[i]
    print(max(a[n][1], a[n][2]))
