'''
어떤 요소를 이진탐색 mid로 돌릴지
mid = 두 공유기 사이 거리
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, c = map(int, input().split())
house = [int(input()) for i in range(n)]
house.sort()

left = 1
right = house[n-1] - house[0]

lengths = []
def bs(left, right):
    mid = (left+right)//2
    wifi = []
    wifi.append(house[0])
    count = 1 # 설치한 공유기 개수
    x = house[0] + mid

    # (c-1)개 공유기 설치
    for i in range(1, n):
        if house[i] >= x:
            wifi.append(house[i])
            count+=1
            x = house[i] + mid
    if lengths and lengths[-1] == mid:
        return
    if count >= c:
        lengths.append(mid)
        bs(mid+1, right)
    else:
        bs(left, mid-1)
bs(left, right)
print(max(lengths))






