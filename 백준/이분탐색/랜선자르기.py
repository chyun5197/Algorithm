import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# n개를 만들수 있는 최대 길이
k, n = map(int, input().split())
lan = [int(input()) for i in range(k)]
right = max(lan)

# sums = []
length = []
def b(left, right):
    mid = (left+right)//2
    sum = 0
    for i in range(k):
        sum += lan[i]//mid
    if length and length[-1] == mid:
        return
    if sum>=n:
        # sums.append(sum)
        length.append(mid)
        b(mid + 1, right)
    elif sum < n:
        b(left, mid-1)

b(1, right)
# print(sums)
print(max(length))