a = [1,2,3]
b = a # 같은 객체
a.append(4)
print(b)
print(a==b) # ==은 스칼라 비교
print(a is b) # is는 같은 객체인지 비교
print('='*20)
###################################
a = [1,2,3,4]
b = list(a) # 복사하여 다른 객체
print(a==b)
print(a is b)
print('='*20)

import copy
a = [[1,2],3,4]
b = copy.copy(a) # 얕은복사
c = copy.deepcopy(a) # 깊은복사

a[-1] = 10
a[0][0] = 10
print(b) # 영향O
print(c) # 영향X
print('='*20)
###################################
a = [1,2,3,4]
print(id(a))
a.append(5)
print(id(a))
print()

def test(list):
    print('함수내부:', id(list))
    list.append(5)
    print('append:', id(list))
    list[0] = 100
    print('인덱싱:', id(list))
    list.extend(['확', '장'])
    print('update:', id(list))
    list += [10,20]
    print('+=:', id(list))
    list = list + [10,20] # 이것만 다름. 리스트 새로 생성(지역변수 선언)
    print('= list + []:', id(list))
k = [1,2,3,4]
print('원본:', id(k))
print('======함수 실행======')
test(k)
print(k)
print('='*20)
###################################
n = 10
k = [1,2,3,4,5,6,7,n]
print(k)
n = 500
print(k) # 안바뀜. 새로 넣어야함

unit = 0
a = k[unit:unit+3]
print(a, id(a))
unit += 2
print(a) # 안바뀜. 새로 넣어야함
print('='*20)
###################################
# 출력관련 Asterisk(*)로 리스트 압축 해제
k = [1,2,3,4,5]
print(*k, sep='\t')
m = {'a': 1, 'b': 2}
print(*m)
print(*m.values())
print(*m.items())

p = [1,2,3,4,5]