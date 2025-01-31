a = [
[1, 0, 0],
[0, 2, 3]
]

b=[
[1, 0],
[0, 2]
]

def rotate(k): # 전체 시계방향 회전
    row = len(k)
    col = len(k[0])
    tmp = [[] for _ in range(col)] # k의 열개수만큼 생성 tmp에 행 생성
    for j in range(col): # 열
        for i in range(row): # 행
            tmp[j].append(k[row-i-1][j])
    return tmp

r1 = rotate(b)
r2 = rotate(r1)
r3 = rotate(r2)
r4 = rotate(r3)
print(r1)
print(r2)
print(r3)
print(r4)

# 추가 - 배열의 특정 구간을 회전
# https://velog.io/@danbibibi/2차원-배열에서-90도-회전-알고리즘