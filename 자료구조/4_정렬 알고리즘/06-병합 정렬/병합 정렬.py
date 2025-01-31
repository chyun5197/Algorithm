'''
# 정렬된 두 리스트의 병합
2개의 정렬된 각 부분 리스트의 첫 번째 원소(i=left, j=mid+1)부터 시작하여 오른쪽으로 진행한다.
a[i]와 a[j]를 비교하여 더 작은 쇼로를 임시 리스트 tmp에 복사하고 인덱스를 증가시킨다.
이 과정이 리스트 하나의 모든 원소가 복사될 때까지 반복되고, 마지막으로 다른 리스트의 남은 원소들을 모두
임시 리스트로 복사하면서 병합을 종료한다.

# 병합 정렬(merge sort)
위의 과정을 분할된 최소 단위의 각 부분 리스트부터 정렬하며 병합을 진행한다.
병합 정렬은 입력의 구성에 상관없이 동일한 시간에 정렬되어 안정적이다. O(nlogn)
'''
def merge_sort(a, left, right): # O(nlogn)
    if left<right:
        mid = (left+right)//2 # 중간 지점 인덱스
        merge_sort(a, left, mid) # 왼쪽 리스트 정렬
        merge_sort(a, mid+1, right) # 오른쪽 리스트 정렬
        merge(a, left, mid, right) # 병합


# 두 리스트를 병합하기
def merge(a, left, mid, right):
    i = left # 왼쪽 리스트의 인덱스
    j = mid + 1 # 오른쪽 리스트의 인덱스
    t = left # 병합을 위한 임시 리스트의 인덱스
    tmp = [0] * len(a) # a와 같은 크기의 임시 리스트
    while i <= mid and j <= right: # 양쪽중 인덱스가 끝에 닿을 때까지
        if a[i] <= a[j]: # 양쪽에서 더 작은 값 탐색
            tmp[t] = a[i] # 임시 리스트에 작은값 삽입
            i += 1 # 왼쪽 리스트 인덱스 증가
        else:
            tmp[t] = a[j]
            j += 1 # 오른쪽 리스트 인덱스 증가
        t += 1 # 임시 리스트 인덱스 증가

    while i <= mid: # 왼쪽 리스트에 원소가 남은 경우
        tmp[t] = a[i]
        t += 1
        i += 1

    while j <= right: # 오른쪽 리스트에 원소가 남은 경우
        tmp[t] = a[j]
        t += 1
        j += 1

    # 임시 리스트에 저장된 결과를 원래의 리스트 a에 복사
    a[left:right+1] = tmp[left:right+1]

# 두 리스트 병합하기
arr = [1,3,7,8,2,4,5,9]
merge(arr, 0, (len(arr)-1)//2, len(arr)-1) # (list, 0, 3, 7)
print(arr)
print()

# 병합 정 시행
k = [5,6,4,8,3,7,9,0,1,5,2,3]
merge_sort(k, 0, len(k)-1)
print(k)