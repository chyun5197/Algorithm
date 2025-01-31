def rotate(k): # 전체 시계방향 회전
    row = len(k) # 행 길이
    col = len(k[0]) # 열 길이
    tmp = [[] for _ in range(col)] # k의 열개수만큼 생성 tmp에 행 생성
    for j in range(col):
        for i in range(row):
            tmp[j].append(k[row-i-1][j])
    return tmp

def solution(key, lock):
    import copy
    k = copy.deepcopy(key) # 열쇠의 돌기부분만 잘라와야함
    l = copy.deepcopy(lock) # 자물쇠의 빈부분만 잘라와야함

    # key 깎
    while True: # 위 깎
        if 1 in k[0]:
            break
        else:
            del k[0]

    while True: # 아래 깎
        if 1 in k[-1]:
            break
        else:
            del k[-1]

    while True: # 왼 깎
        temp = [i[0] for i in k]
        if 1 in temp:
            break
        else:
            for i in k:
                del i[0]

    while True: # 오 깎
        temp = [i[-1] for i in k]
        if 1 in temp:
            break
        else:
            for i in k:
                del i[-1]
    ################################################
    # lock 깎
    while True:  # 위 깎
        if 0 in l[0]:
            break
        else:
            del l[0]

    while True:  # 아래 깎
        if 0 in l[-1]:
            break
        else:
            del l[-1]

    while True:  # 왼 깎
        temp = [i[0] for i in l]
        if 0 in temp:
            break
        else:
            for i in l:
                del i[0]

    while True:  # 오 깎
        temp = [i[-1] for i in l]
        if 0 in temp:
            break
        else:
            for i in l:
                del i[-1]

    # 확인코드
    # for a in k:
    #     print(a)
    # print()
    # for a in l:
    #     print(a)
    print(k)  # key깎 확인
    print(l)

    # 안되는 조건: 1. key 1개수 < lock 0개수
    #           2. 회전포함 행렬 크기 <
    # 안됨1
    key1 = 0
    lock0 = 0
    for a, b in zip(k, l):
        key1 += a.count(1)
        lock0 += b.count(0)
    if key1 < lock0:
        return False

    # 안됨2
    rowK, colK = len(k[0]), len(k)
    rowL, colL = len(l[0]), len(l)
    if not (rowK>=colL and colK>=rowL):
        return False
    if not (rowK>=rowL and colK>=colL):
        return False

    # 전부 끼워보기
    r0 = copy.deepcopy(l)
    r1 = rotate(l)
    r2 = rotate(r1)
    r3 = rotate(r2)

    # 원본
    check = 'o'
    for i in range(len(l)): # 행
        for j in range(len(l[0])): # 열
            r0[i][j] += k[i][j]
        if 0 in r0[i]:
            check = 'x'
            break
    if check=='o':
        return True

    # r1
    check = 'o'
    for i in range(len(l)): # 행
        for j in range(len(l[0])): # 열
            r1[i][j] += k[i][j]
        if 0 in r1[i]:
            check = 'x'
            break
    if check=='o':
        return True

    # r2
    check = 'o'
    for i in range(len(l)): # 행
        for j in range(len(l[0])): # 열
            r2[i][j] += k[i][j]
        if 0 in r2[i]:
            check = 'x'
            break
    if check=='o':
        return True

    # r3
    check = 'o'
    for i in range(len(l)): # 행
        for j in range(len(l[0])): # 열
            r3[i][j] += k[i][j]
        if 0 in r3[i]:
            check = 'x'
            break
    if check=='o':
        return True

    return False


key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]
lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

# key = [[0, 1, 0, 0],
#        [0, 0, 1, 0],
#        [0, 1, 0, 0],
#        [0, 0, 0, 0]]

# lock = [[1, 1, 1],
#         [1, 1, 0],
#         [1, 0, 1]]

# lock = [[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 0, 1, 1],
#         [1, 0, 1, 0]
#         ]
print(solution(key, lock))