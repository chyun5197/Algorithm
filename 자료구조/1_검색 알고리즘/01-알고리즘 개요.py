''' &초기화 선행
# 알고리즘
문제를 해결하기 위한 단계적인 절차
문제를 해결하기 위한 프로그램 명령어의 집합

# 효율적인 알고리즘이란?
알고리즘이 수행을 시작하여 결과가 도출될 때까지
실행 시간이 짧을수록(시간복잡도), 사용되는 컴퓨터 내의 메모리양이 적을수록(공간복잡도) 효율적이다.
참고) 컴파일 언어(C/C++, Java)가 인터프리터 언어(Python/Javascript)보다 실행속도가 빠르다

# 공간 복잡도(Space Complexity) @오늘날 메모리공간 언급 @변수가 만들어지는 공간
프로그램을 실행시켜 완료하는데 필요한 메모리양(자원)을 나타낸다.
- 측정방법: 문제의 크기(n)에 따른 메모리 사용량을 byte로 계산
- ex: S(n) = 100n bytes
@ 오늘날 메모리 넘침. 공간 효율성 중요도 낮아짐.
@ 메모리 사용량 줄이기 쉽지않기에 알고리즘 높이는건 시간복잡도쪽

# 시간 복잡도(Time Complexity)
프로그램을 실행시켜 완료하는데 필요한 시간을 나타낸다.
- 측정방법: 실제 실행 시간 측정 or 알고리즘이 수행하는 연산의 수를 계산
- 계산된 결과를 점근적(대략적)으로 표현
- ex: T(n) = n steps

# 동일한 알고리즘에서도 입력 데이터에 따라 실행 시간이 다르다
최선의 경우(Best Case): 실행 시간이 가장 적은 경우
평균적인 경우(Average Case): 모든 입력의 발생 확률을 고려한 평균 실행 시간 @구하기 어려움
최악의 경우(Worst Case): 실행 시간이 가장 오래 걸리는 경우

# 시간 복잡도 함수 T(n)
모든 데이터 입력에 대해 걸리는 최대 시간(Worst Case) &go
ex) T(n) = 3n + 5

# 빅오 표기법 (Big-O, 점근 표기법) @그래프
일반적으로 알고리즘의 시간복잡도를 나타내는데 빅오 표기법을 사용한다.
연산의 횟수를 대략적(점근적)으로 표기하기 위해 사용하다.
정확한 연산 횟수가 아닌 입력 크기에 따른 알고리즘의 일반적인 증가율을 분석한다.

@입력이나 실행 상황에 따라 절대적인 수행시간은 의미가 없을 수 있다.
                n<-10   n<-100    n<-1000  n이 커질수록
A: n^2 + 2n     120     10200   1,002,000 (10^6+2000)
B: 100n         1000    10000     100,000 (10^5)

# 실제 수행시간 -> 빅오 시간복잡도
T(n) = 5 -> O(1)
T(n) = 2n +3 -> O(n)
T(n) = 3n^2 + 100 -> O(n^2)

'''
# O(1): 1부터 n까지의 합을 구하는 알고리즘
n = 10
total = n * (n + 1) // 2 # 실행횟수 4 (곱셈, 덧셈, 나눗셈, 대입)
print('T(n) = 4')
print("O(n) = 1") # 상수 시간
print('='*30)

# O(n): 선형 탐색으로 특정 데이터 찾기
nums = [6, 4, 3, 2, 1, 5, 8, 7]
n = len(nums) # 리스트 개수: n개
search = 1 # 탐색할 키
time = 0

for i in range(n): # 실행횟수 n
    time+=1
    if nums[i] == search: # 실행횟수 n
        find = nums[i] # 실행횟수 1
        break
print("반복횟수 = ", time) # 대략적 계산
print("최대 반복횟 = ",len(nums))
print("T(n) = 2n + 2") # T(n) = 2n + 2
print("O(n) = n") # 반복문 1개
print("="*30)

# O(n^2): 중복되는 값이 있는지 탐색하기
nums = [2, 3, 2, 1, 5, 4, 3, 6]
# nums = [2, 3, 20, 1, 5, 4, 6, 6]
n = len(nums) # 리스트 개수: n개
time = 0
exit = 0
for i in range(n):
    for j in range(i+1, n):
        time+=1
        if nums[i] == nums[j]:
            print("중복값:", nums[i])
            exit = 1 # 중복값을 찾으면 외부for문을 탈출할 코드
            break # 중복값을 찾으면 내부for문 탈출
    if exit == 1:
        break

print("반복횟수 = ", time)
print("최대 time = ", 7+6+5+4+3+2+1) # n(n-1)/2
print("O(n^2)") # 반복문 2번
print("="*30)

# O(log n), O(n log n): 정렬 알고리즘에서 많이 사용

#######################################################
# 코드 실행시간 측정 by time모듈 이용
import time as t
print(t.time())

start = t.time() # 시작시간
list = []
for i in range(10000): # 리스트에 원소 10000개 삽입
    list.append(i)

end = t.time() # 종료시간
minute = end - start # 실제 수행시간

print(f'실행시간 = {minute:.6f}초')
print("="*30)
#######################################################
# 리스트에 랜덤한 정수 5000개 삽입
import random as rd
nums = []
for i in range(5000):
    nums.append(rd.randint(1,100))

# 오름차순으로 정렬하는 코드 구현하기
n = len(nums)
start = t.time() # 시작시간
for i in range(n): # O(n^2)
    for j in range(i+1, n):
        if nums[i] > nums[j]: # swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        # if nums[i] > nums[j]:
        #     nums[i], nums[j] = nums[j], nums[i]
end = t.time() # 종료시간
minute = end - start # 실제 수행시간
print(f"오름차순 정렬 수행시간(구현코드) = {minute:.7f}초")
# print("오름차순 정렬:", nums)

#######################################################
# 파이썬 내장함수로 오름차순하기
import random as rd
nums = []
for i in range(5000):
    nums.append(rd.randint(1,100))

start = t.time() # 시작시간
nums.sort() # https://github.com/python/cpython
end = t.time() # 종료시간
minute = end - start # 실제 수행시간
print(f"오름차순 정렬 수행시간(내장함수) = {minute:.7f}초")

# @언어의 종류 go






