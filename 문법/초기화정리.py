print(ord('A') == 65)
print(chr(65+25))
print(chr(97+25))

INF = int(1e9) # 최대값(무한대) 설정

sums = [0,1,2,3,4]
print(*sums, sep='\n')

# 깊은 복사
import copy
x = [[1,2], [3,4]]
y = copy.deepcopy(x) # deepcopy(): 깊은 복사. 원소 값만 복사
print("y =", y)

y[0][0] = 9
print("--------변경 후--------")
print("x =", x) # 원본 리스트의 원소는 그대로
print("y =", y) # 복사 받은 리스트의 원소만 변경
