'''
# 선택 정렬(selection sort)
배열에서 가장 작은 원소를 하나씩 선택하여 순서대로 저장하는 알고리즘
'''
def selection_sort(a): # O(n^2) | 비교횟수: n(n-1)/2 고정
    n = len(a)
    for i in range(n-1): # i는 정렬되지 않은 부분의 시작 인덱스(0 ~ n-2)
        min = i # 최소값이 될 원소의 인덱스
        for j in range(i+1, n): # j는 (i+1 ~ n-1)
            if a[j] < a[min]: # (i+1)부터 (n-1)까지의 원소 중에서 최솟값의 인덱스를 구함
                min = j
        a[i], a[min] = a[min], a[i] # 정렬되지 않은 부분의 맨 앞의 원소와 최소값 원소를 교환

k = [6,4,8,3,1,9,7]
selection_sort(k)
print(k)

