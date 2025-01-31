import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀함수 깊이 늘리기 (원래는 1000까지로 얕음)

n, m = map(int, input().split())
tree = list(map(int, input().split()))

h = []
def binarySearch(left, right):
    mid = (left+right)//2

    # 딱 떨어지지 않는경우 무한반복에서 빠져나와야함
    if len(h) and mid == h[-1]: # 같은값 반복 삽입일때를 무한반복 시작으로 판정하여 탈출
        return

    sum = 0
    for i in range(n):
        if tree[i]>mid:
            sum += tree[i] - mid
    if sum == m:
        h.append(mid)
        return
    elif sum > m:
        h.append(mid)
        binarySearch(mid+1, right)
    else:
        binarySearch(left, mid-1)
binarySearch(0, max(tree))
print(max(h))
# while True
