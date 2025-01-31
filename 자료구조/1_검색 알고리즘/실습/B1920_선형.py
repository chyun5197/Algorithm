# 백준1920
# 리스트a에 리스트b의 값들이 있는지1/없는지0 한줄에 하나씩 출력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 선형 탐색 알고리즘 (시간초과)
for numB in b:
    find = False
    for numA in a:
        if numA == numB:
            find = True
    if find:
        print(1)
    else:
        print(0)

# 리스트 in연산자 사용 (시간초과)
for num in b:
    if num in a:
        print(1)
    else:
        print(0)

# import sys
# input = sys.stdin.readline