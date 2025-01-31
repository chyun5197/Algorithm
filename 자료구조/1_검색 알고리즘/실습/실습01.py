'''
Q1)	업다운 게임을 만들어 봅시다.
	랜덤으로 1~100 사이의 정답 숫자를 미리 만들어 놓고,
	사용자가 숫자를 입력하여 정답을 맞추도록 코드를 작성하시오.

	<게임의 상태>
	[업] 사용자가 정답보다 낮은 값을 입력한 경우
	[다운] 사용자가 정답보다 높은 값을 입력한 경우
	[정답] 사용자가 정답과 같은 값을 입력한 경우 => 게임 종료

	사용자가 정답을 입력하기 전까지 무한반복을 한다.
	게임 종료시 총 입력한 횟수를 화면에 출력한다.

	↓ Console ↓
	숫자 입력: 50
	[다운]
	숫자 입력: 25
	[업]
	숫자 입력: 37
	[업]
	숫자 입력: 43
	[다운]
	숫자 입력: 40
	[다운]
	숫자 입력: 38
	[정답]
	시도한 총 횟수 = 6

Q2) 위와 동일한 업다운 게임을 만드는데 이진탐색 코드를 이용하여
    프로그램이 숫자 입력을 자동으로 시행하여 정답을 구하도록 코드를 구현해보자

    ↓ Console ↓
    검색 숫자: 50
    [업]
    검색 숫자: 75
    [다운]
    검색 숫자: 62
    [업]
    검색 숫자: 68
    [업]
    검색 숫자: 71
    [정답]
    시도한 총 횟수 = 5
'''
# 1~100사이 랜덤 정수 생성하기
import random as rd
answer = rd.randint(1,100) # 정답 숫자

# # Q1
# count = 0
# while True:
#     pick = int(input("숫자 입력: "))
#     count+=1
#
#     if answer == pick:
#         print("[정답]")
#         print(f"시도한 총 횟수 = {count}")
#         break
#     elif answer < pick:
#         print("[다운]")
#     else:
#         print("[업]")
#

# 이진 탐색 알고리즘 함수
def binary_search(arr, key, left, right):
    count = 0
    while left<=right:
        count+=1
        mid = (left+right)//2
        print(f'검색 숫자: ', arr[mid])
        if key == arr[mid]:
            print("[정답]")
            break
        elif key > arr[mid]:
            print("[업]")
            left = mid + 1
        else:
            print("[다운]")
            right = mid - 1
    return count

# Q2
nums = [i for i in range(1,101)] # 리스트에 1~100 숫자 초기화
low = 0 # 최소값 인덱스
high = 99 # 최대값 인덱스
c = binary_search(nums, answer, low, high)
print(f'시도한 총 횟수 =', c)

# list = []
# for i in range(1, 101):
#     list.append(i)

# print(list)


# def binary_search(nums, search):
#     left = nums[0]
#     right = nums[len(nums)-1]
#     count = 0
#     while left <= right:
#         count+=1
#         mid = (left + right) // 2
#         print(f"검색 숫자: {mid}")
#         if search == nums[mid]:
#             print("[정답]")
#             print(f"시도한 총 횟수 = {count}")
#             break
#         elif search < nums[mid]:
#             print("[다운]")
#             right = mid - 1
#         else:
#             print("[업]")
#             left = mid + 1
# binary_search(list, answer)



