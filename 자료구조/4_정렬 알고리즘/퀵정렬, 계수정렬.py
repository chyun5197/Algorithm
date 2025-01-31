#== 퀵 정렬 ==# 평균적으로 O(NlogN)
# 수정 파이썬 퀵 정렬 코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1: # 리스트가 하나 이하의 원소만 담고 있으면 종료
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))

#== 계수 정렬(count sort) ==# O(N+K)
# 모든 원소의 값이 0 이상이라고 가정
array = [5,7,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1) # 모든 범위의 인덱스를 포함하는 리스트 선언
for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')
