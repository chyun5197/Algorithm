# 음료수얼려먹기와 유사
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 재귀함수 깊이 늘리기 (원래는 1000까지로 얕음)

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[x][y] == 1: # 방문하지 않았다면
        graph[x][y] = 0 # 방문처리
        # 상하좌우 모두 재귀 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 방문처리가 되면 리턴 True
    return False # 0인곳은 리턴 False

t = int(input()) # 시행 케이스
for pp in range(t):
    m, n, k = map(int, input().split()) # 가로 세로 개수
    graph = [[0]*m for i in range(n)]
    target = []
    for i in range(k):
        y,x = map(int, input().split()) # 좌우, 상하
        graph[x][y] = 1 # graph[상하][좌우]
        target.append((x,y))

    # 모든 노드에 대하여 확인하기
    count = 0
    for k in target:
        i, j = k
        if dfs(i, j):
            count+=1
    # for i in range(n):
    #     for j in range(m):
    #         if dfs(i, j):
    #             count += 1
    print(count)
