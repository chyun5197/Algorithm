'''
로직)
2를 빨리 찾고 -> 주위 0감염 1스탑 or 양옆 이미 감염이면 스탑
모든 2 주변 감염 끝 -> 남은 0은 모두 안전

반례)
3 3
2 2 0
0 0 0
0 0 0

정답 4
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) 

# 세로, 가로
n, m = map(int, input().split())
graph = []
virus = [] # 바이러스(2) 위치 저장
num0 = [] # 0이 들어있는 좌표 저장
a = 0
for i in range(n):
    k = list(map(int, input().split()))
    graph.append(k)
    for b in range(m):
        if k[b] == 2:
            virus.append((a,b))
        elif k[b] == 0:
            num0.append((a,b))
    a+=1

# print(virus)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

import copy
result = copy.deepcopy(graph)

'''
# case1
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

# case2
4 6
0 0 0 0 1 0
1 0 0 1 0 2
1 1 1 0 0 2
0 0 0 1 0 2

# case3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
result[0][1] = 1
result[1][0] = 1
result[3][5] = 1

# result[0][4] = 1
# result[1][3] = 1
# result[3][3] = 1

# result[-1][2] = 1
# result[-2][1] = 1
# result[-3][0] = 1
'''

# dfs 감염여부처리
def dfs(x, y): # 2의 위치(세로, 가로)
    # for kk in result:
    #     print(kk)
    # print()
    if result[x][y] == 0:
        result[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m: # 영역 외 제외
            continue
        if result[nx][ny] == 1 or result[nx][ny] == 2: # 벽이나 이미 감염은 제외
            continue
        dfs(nx, ny)

# 안전 영역 개수 탐색
def getSafe(result):
    safe = 0
    for i in result:
        # print(i)
        safe += i.count(0)
    return safe

# 0에 울타리 설치(조합)
from itertools import combinations
max = 0
for zeros in combinations(num0, 3):
    # print(zeros)
    for zero in zeros:
        result[zero[0]][zero[1]] = 1
    for i in virus:  # 기존 2마다 주변 모두 감염 처리
        dfs(i[0], i[1])
    nowSafe = getSafe(result)
    if nowSafe > max:
        max = nowSafe
    result = copy.deepcopy(graph)
print(max)


