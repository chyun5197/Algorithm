'''
# S초 동안 반복
# 바이러스 위치 담고 있어야함
# 좌표 전체 확인 -> (1~k까지 전염 -> 새로 생긴 바이러스 위치 체크) s초 동안 반복
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# nXn 행렬, 바이러스 번호k까지
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split()) # s초 후 (x,y) 좌표의 바이러스 종류 알아내기

# virus = [[] for i in range(k+1)]
from collections import deque
virus = [deque([]) for i in range(k+1)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 좌표에서 시작 바이러스 체크
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i, j))

while s: # s초 동안
    for num in range(1, k+1): # 모든 바이러스 위치 1번부터 4방향 전염
        nextVirus = []
        for xy in virus[num]:
            for i in range(4):  # 모든 방향
                nx = dx[i] + xy[0]
                ny = dy[i] + xy[1]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] > 0:
                    continue
                graph[nx][ny] = num
                nextVirus.append((nx,ny))
        virus[num] = deque(nextVirus)
    s-=1
    # print(virus)  # 바이러스 확인
    # for i in graph:  # 그래프 확인
    #     print(i)
    # print()
print(graph[x-1][y-1])

