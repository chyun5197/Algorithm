'''
itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
            특히 순열, 조합 라이브러리
heapq: 힙 자료구조. 우선순위 큐 기능
bisect: 이진 탐색
collections: 덱, 카운터
math: 팩토리얼, 제곱근, 최대공약수, 삼각함수
https://land-turtler.tistory.com/152 더 추가
'''
# eval()
ret = eval("(3+5)*7")
print(ret)

############## 람다 표현식 ###############
num = (lambda a,b:a+b)(3, 7)
print(num)

arr = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def myKey(x):
    return x[1] # 두번째 원소
k = sorted(arr, key=myKey) # key = 두번째 원소 기준으로 정렬
print(k) 
k = sorted(arr, key=lambda x: x[1], reverse=True)
print(k)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
ret = map(lambda a,b:a+b, list1, list2)
print(list(ret))
print('='*20)

############## itertools ###############
data = ['A', 'B', 'C']

# 순열(순서 고려 나열) Permutation
from itertools import permutations
print(list(permutations(data, 2))) # 모든 순열 구하기
print()

# 조합(순서X 뽑기) Combination
from itertools import combinations
print(list(combinations(data, 2))) # 몇개 뽑을지
print()

# 중복 허용하여 2개를 뽑는 모든 순열 구하기
from itertools import product
print(list(product(data, repeat=2)))
print()

# 중복 허용하여 2개를 뽑는 모든 조합 구하기
from itertools import combinations_with_replacement
print(list(combinations_with_replacement(data, 2)))
print('='*20)

############## counter ###############
# 등장 횟수를 세는 기능 제공
from collections import Counter
k = ['red', 'blue', 'red', 'green', 'blue', 'blue']
ct = Counter(k)
print(ct['blue'])
print(ct['green'])
print(dict(ct)) # 딕셔너리로 변환해서 사용 가능
print('='*20)

############## math ###############
# 최대 공약수는 gcd() 함수
import math
def lcm(a,b): # 최소공배수(LCM)
    return a*b // math.gcd(a,b)
print(lcm(21,14))
print((lambda a,b:a*b//math.gcd(a,b))(10, 15))
