'''
# 삽입 정렬(insert sort)
더 앞쪽의 정렬된 부분 배열에 다음 원소를 알맞은 위치에 삽입하는 알고리즘
정렬되지 않은 부분의 맨 앞 원소를 정렬된 부분의 알맞은 위치에 삽입하는 작업을 (n-1)번 반복한다.
'''
def insert_sort(a): # O(n^2) | 비교횟수: n(n-1)/2
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i] # 삽입할 원소를 복사해놓음
        while j > 0 and a[j-1] > tmp: # 왼쪽 끝까지 가거나 tmp보다 작지 않을 때까지 계속 진행
            a[j] = a[j-1] # 오른쪽으로 한칸 땡김
            j -= 1 # 탐색을 다음 왼쪽으로 넘어감
        a[j] = tmp # 땡겨서 빈자리에 빼놓은 tmp원소 삽입

k = [6,4,1,7,3,9,8] # do it
insert_sort(k)
print(k)
