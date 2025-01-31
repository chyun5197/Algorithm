# 백준14395
import sys
input = sys.stdin.readline
s = input().strip()
a = 0 # 전부 0으로 바꾸는 경우
b = 0 # 전부 1로 바꾸는 경우
if s[0] == '1':
    a += 1
else:
    b += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            a += 1
        else:
            b += 1
print(min(a,b))