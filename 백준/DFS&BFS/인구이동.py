import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 재귀함수 깊이 늘리기 (원래는 1000까지로 얕음)

n, l, r = map(int, input().split())
board = []
merges = [[0] * n for i in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))

dx = (-1,1,0,0)
dy = (0,0,-1,1)
day = 0
while True:
    check = True
    sum = [0] * (n*n+1)
    cnt = [0] * (n*n+1)
    def dfs(x, y, num):
        global check
        if x<0 or x>=n or y<0 or y>=n:
            return
        if merges[x][y] != 0: # 이미 연결됬으면 패스
            return
        merges[x][y] = num
        sum[num] += board[x][y]
        cnt[num] += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            elif merges[nx][ny] != 0:  # 이미 연결됬으면 패스
                continue
            elif l <= abs(board[x][y]-board[nx][ny]) <= r:
                check = False # 이동이 한번이라도 일어나면 종료가 아님
                dfs(nx, ny, num)
                merges[nx][ny] = num

    num = 1
    for i in range(n): # 국경 공유
        for j in range(n):
            if merges[i][j] == 0:
                dfs(i, j, num)
                num += 1

    for i in range(n*n+1): # 통합 인구수 미리 계산
        if sum[i] != 0:
            sum[i] = sum[i]//cnt[i]

    for i in range(n): # 인구 이동
        for j in range(n):
            board[i][j] = sum[merges[i][j]]

    if check:
        break

    # 확인코드
    # print('='*10)
    # for i in board:
    #     print(i)
    # for i in merges:
    #     print(i)

    day += 1
    merges = [[0] * n for i in range(n)]
print(day)


