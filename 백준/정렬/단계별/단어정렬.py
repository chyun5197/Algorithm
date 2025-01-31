import sys
input = sys.stdin.readline
n = int(input())
msg = {input().rstrip() for i in range(n)}
msg = list(msg)
msg.sort(key=lambda x:[len(x), x])
for i in msg:
    print(i)