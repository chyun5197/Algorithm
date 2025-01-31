from itertools import combinations
import copy
n = int(input())
graph = []
blanks = []
teachers = []
for i in range(n):
    k = input().split()
    graph.append(k)
    for j in range(n):
        if k[j] == 'X':
            blanks.append((i, j))
        elif k[j] == 'T':
            teachers.append((i, j))

# for i in range(n): # 그래프 확인
#     print(graph[i])
# print(blanks) # 빈칸 확인
# print(teachers) # 빈칸 확인

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def watcher(x,y,temp): # 선생 한명 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        while True:
            if nx<0 or nx>=n or ny<0 or ny>=n:
                break
            elif temp[nx][ny] == 'S':
                return True
            elif temp[nx][ny] == 'O' or temp[nx][ny]== 'T': # 벽 또는 선생 마주치면
                break
            nx += dx[i]
            ny += dy[i]
    return False


check = True # 발견
for blank in combinations(blanks, 3): # 3개 벽설치 모든 조합
    temp = copy.deepcopy(graph)
    isFind = []
    for wall in blank: # 벽설치
        temp[wall[0]][wall[1]] = 'O'
    for teacher in teachers: # 모든 선생 탐색
        result = watcher(teacher[0], teacher[1], temp)
        isFind.append(result)
        if result: # 한명이라도 발각되면 넘어감
            break
    if True not in isFind:
        print('YES')
        check = False
        # for i in temp: # 그래프 확인
        #     for j in i:
        #         print(j, end=' ')
        #     print()
        break
if check:
    print('NO')


