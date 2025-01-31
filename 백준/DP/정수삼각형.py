'''
단계별 모든 값 위치에 왔을때의 최대값을 다 저장해 놔야함
'''
import sys
input = sys.stdin.readline

n = int(input())
tri = []
d = []
for i in range(1, n+1):
    nums = list(map(int, input().split()))
    tri.append(nums)
    d.append([0]*len(nums))

# print(d)
import copy
d[0][0] = copy.deepcopy(tri[0][0])
for i in range(1, n): # i번째줄
    for j in range(i+1): # j는 각 줄 0,1,i-1번째
        if j == 0: # 맨앞
            d[i][j] = tri[i][j] + d[i-1][j] # 전줄 본인 위치랑 더하기
            continue
        elif j == i: # 맨뒤
            d[i][j] = tri[i][j] + d[i-1][j-1] # 전줄 본인 이전 위치랑 더하기
            continue
        # 중간 값들) 비교할건 j 본인 위치와 j-1 둘중 큰걸로 저장
        d[i][j] = max(tri[i][j] + d[i-1][j], tri[i][j] + d[i-1][j-1])

for i in range(n):
    print(d[i])
print(max(d[n-1]))


