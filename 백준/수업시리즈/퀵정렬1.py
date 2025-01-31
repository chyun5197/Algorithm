import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

a, k = map(int, input().split())
arr = list(map(int, input().split()))


def quick_sort(a, left, right): # 2 O(nlogn)
    if left<right:
        q = partition(a, left, right) # 분할
        quick_sort(a, left, q-1) # 왼쪽 부분 배열 정렬 (left, pr)
        quick_sort(a, q+1, right) # 오른쪽 부분 배열 정렬 (pr+2, right)

# 리스트를 두 그룹으로 나누기
def partition(a, left, right): # 1
    global k
    pl = left # 왼쪽 커서
    pr = right # 오른쪽 커서
    x = a[(left+right)//2] # 피벗(가운데 원소)

    while pl<=pr: # 배열 a를 피벗 x의 양옆에 두 그룹으로 나누기
        while a[pl] < x: pl += 1 # 왼쪽 원소가 피벗보다 작으면 다음 커서 선택
        while a[pr] > x: pr -= 1 # 오른쪽 원소가 피벗보다 크면 다음 커서 선택
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            k -= 1
            print(min(a[pl], a[pr]), max(a[pl], a[pr]))
            pl += 1
            pr -= 1
    return pr + 1

quick_sort(arr, 0, len(arr)-1)