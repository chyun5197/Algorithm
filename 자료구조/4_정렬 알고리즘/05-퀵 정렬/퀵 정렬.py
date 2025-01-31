'''
# 분할 정복(divide and conquer)
https://cinux.tistory.com/13
분할 정복이란 주어진 문제를 여러개의 작은 부분 문제들로 나누고,
이들을 각각 해결한 후 결과들을 모아서 원래의 문제를 해결하는 전략이다.
정렬이나 탐색에서 매우 효과적이다. (퀵, 병합, 이진)

분할(divide): 문제를 더이상 분할할 수 없을 때까지 동일한 유형의 여러 하위 문제로 나눈다.
정복(conquer): 가장 작은 단위의 하위 문제를 해결하여 정복한다.
조합(combine): 하위 문제에 대한 결과를 원래 문제에 대한 결과로 조합한다.

# 퀵 정렬(quick sort)
평균적으로 매우 빠른 수행 속도를 가지는 정렬 방법이다. 분할 정복.
기준이 되는 값(피벗)을 선택하여 이보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 이동(분할)시키는 방식.
=> 양쪽 부분 배열을 재귀 함수로 계속적으로 분할 정복하여 정렬.

백준 퀵정렬1 의사코드
@ 불필요한 데이터의 이동을 줄이고 먼 거리의 데이터를 교환하며,
한번 결정된 피벗들이 추후 연산에서 제외되어 매우 빠름.
'''
def quick_sort(a, left, right): # 2 O(nlogn)
    if left<right:
        q = partition(a, left, right) # 분할
        quick_sort(a, left, q-1) # 왼쪽 부분 배열 정렬 (left, pr)
        quick_sort(a, q+1, right) # 오른쪽 부분 배열 정렬 (pr+2, right)

# 리스트를 두 그룹으로 나누기
def partition(a, left, right): # 1
    pl = left # 왼쪽 커서
    pr = right # 오른쪽 커서
    x = a[(left+right)//2] # 피벗(가운데 원소)

    while pl<=pr: # 배열 a를 피벗 x의 양옆에 두 그룹으로 나누기
        while a[pl] < x: pl += 1 # 왼쪽 원소가 피벗보다 작으면 다음 커서 선택
        while a[pr] > x: pr -= 1 # 오른쪽 원소가 피벗보다 크면 다음 커서 선택
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    # 진행 확인코드
    print('\n피벗:', x)
    print(f'(pl, pr) = ({pl}, {pr})')
    print('피벗 이하 그룹:', a[left:pl])
    print('피벗 이상 그룹:', a[pr+1:right+1])
    if pl > pr + 1: print('피벗과 일치하는 그룹:', a[pr+1:pl])
    print('현재 배열:', a)

    return pr+1 #@2후첨 # 다음 피벗의 인덱스를 반환

# 한번 분할 시행
# arr = [1,8,7,4,5,2,6,3,9]
# partition(arr, 0, len(arr)-1)
# print('배열을 두 그룹으로 나누기:', arr)

# 퀵 정렬 시행
# arr = [1,8,7,4,5,2,6,3,9]
k = [5,8,4,2,6,1,3,9,7]
quick_sort(k, 0, len(k)-1)
print('퀵 정렬:', k)
