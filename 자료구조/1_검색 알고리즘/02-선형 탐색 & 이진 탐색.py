'''
# 선형 탐색 알고리즘(Linear Search) @순차탐색
선형 탐색은 선형으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지
맨 앞부터 스캔하여 순서대로 검색 하는 알고리즘이다.
선형 탐색은 무작위로 늘어놓은 데이터 집합에서 검색을 수행한다.

# 이진 탐색 알고리즘(Binary Search)
이진 탐색은 자료가 오름차순이나 내림차순으로 정렬된 배열에서
좀 더 효율적으로 검색할 수 있는 알고리즘이다.
처음 중앙값을 임의의 값으로 선택하여 찾고자 하는 값의 크고 작음을 비교하는 방식이다.
처음 선택한 중앙값이 만약 찾는 값보다 작으면 그 값은 새로운 최솟값이 되고
크면 그 값은 새로운 최댓값이 된다.
이진 탐색은 일정한 규칙으로 늘어놓은 데이터 집합에서 아주 빠른 검색을 수행한다.
'''
# 주어진 자료
nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# nums = [50, 20, 90, 30, 110, 70, 80, 10, 100, 0, 60, 40]

# nums = list(range(0,110+1,10))
# import random
# random.shuffle(nums) # 무작위 데이터일 때
print(nums)

search = 10 # 찾을 데이터 @바꿔가며 앞뒤 비슷
length = len(nums)  # 자료 개수
print("찾을 데이터:",search)
print()

#===== 선형 탐색 알고리즘(Linear Search) =====#
print("======선형 탐색 알고리즘======")
time = 0 # 반복 횟수

for i in range(length):
    time+=1
    if nums[i] == search:
        idx = i
        break # 탐색 성공 후
print("index =", idx)
print("선형탐색 반복횟수 =", time) #@최대 마찬가지
print()

#===== 이진 탐색 알고리즘(Binary Search) =====#
print("======이진 탐색 알고리즘======")
time = 0 # 반복 횟수
left = 0 # 최솟값 인덱스
right = length-1 # 최댓값 인덱스

while left<=right:
    mid = (left+right)//2
    time+=1
    if search == nums[mid]:
        idx = mid
        break # 탐색 알고리즘 성공 후 탈출
    elif search > nums[mid]:
        left = mid+1 # 최솟값 인덱스 조정
    else :
        right = mid-1 # 최댓값 인덱스 조정

print("index =", idx)
print("이진탐색 반복횟수 =", time)
print()
# Prac01 go





