# B2164
from collections import deque
n = int(input())
d = deque([i for i in range(1, n+1)]) # 1234..n 숫자를 리스트로 삽입

num = 1 # 숫자 1부터 플레이 시작
while len(d)!=1: # 큐에 1개 남을 때까지 진행
   if num%2==1: # 1,3,5.. 홀수일 경우 삭제만
       d.popleft()
   else: # 짝수는 뒤로 옮기기
       d.append(d.popleft()) # 맨 앞에 값을 꺼내오면서 뒤에 삽입
   num+=1
print(d[0])