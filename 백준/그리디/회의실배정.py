import sys
input = sys.stdin.readline
n = int(input())
times = []
for i in range(n):
    a, b = map(int, input().split())
    times.append((a, b))
times.sort(key=lambda x: (x[1], x[0]))
# print(*times, sep='\n')

nextEnd = 0
cnt = 0
for prevStart, prevEnd in times:
    if nextEnd <= prevStart:
        cnt+=1
        nextEnd = prevEnd
print(cnt)


