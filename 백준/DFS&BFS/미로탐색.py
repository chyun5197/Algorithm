n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상,하,좌,우
dx = [-1,1,0,0] # 상하
dy = [0,0,-1,1] # 좌우

from collections import deque
def bfs(x, y):
    que = deque()
    que.append((x,y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 1 + graph[x][y]
                que.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))

