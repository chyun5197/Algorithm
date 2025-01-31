n, m = 4,5
# n, m = 15, 14

graph = []
for i in range(n): # 2차원 리스트 입력
    graph.append(list(map(int, input())))
'''
00110
00011
11111
00000
'''
print(graph)

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y): # 세로, 가로
    if x<=-1 or x>=n or y<=-1 or y>= m: # 주어진 범위 벗어나면 즉시 종료
        return False
    if graph[x][y] == 0: # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 해당 노드 방문처리
        # 상하좌우 위치 모두 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # 방문처리가 되면 True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True: # 현재 위치 방문처리 된거면 +1
            result += 1
print(result)






