# Counter 클래스는 해시 가능한 객체를 세는데 사용하는 딕셔너리 서브 클래스
# https://www.guru99.com/ko/python-counter-collections-example.html
from collections import Counter # go to

n = int(input())
a = map(int, input().split())
a = Counter(a) # a = set(a) 집합부터

m = int(input())
b = list(map(int, input().split()))

for num in b:
    if num in a:
        print(1)
    else:
        print(0)