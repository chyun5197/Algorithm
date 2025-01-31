import sys
input = sys.stdin.readline
t = int(input())
n = int(input()) # 팀의 수
graph = [[] for i in range(n+1)]
lastRanks = list(map(int, input().split())) # 작년 랭킹
lastRanks.insert(0,0)
result = []
for i in range(1, n+1):
    result.append((lastRanks[i], i)) # 등수, 팀번호
result.sort(reverse=True)

m = int(input())
for _ in range(m): # 상대 순위 변함
    a, b = map(int, input().split())
print(result)
