n = int(input())
a = list(map(int, input().split()))
a.sort() # 오름차순 정렬

m = int(input())
b = list(map(int, input().split()))

# 이진 탐색 알고리즘
def binary_search(arr, key, left, right): # 이진 탐색 알고리즘 함수
    while left<=right:
        mid = (left+right)//2
        if key == arr[mid]:
            return True
        elif key > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False

for num in b:
    exist = binary_search(a, num, 0, len(a)-1)
    if exist==True:
        print(1)
    else:
        print(0)