'''
# 파이썬 덱 모듈
스택, 큐, 덱의 데이터 삭제와 삽입의 시간복잡도는 항상 O(1)이어야함
하지만 큐, 덱을 구현하는데 사용한 list는 삭제할때 시간복잡도가 O(n)이다.
파이썬 모듈을 사용하면 시간복잡도 O(1)으로 사용 가능.
=> 스택은 리스트로 그대로 사용 / 큐, 덱은 파이썬 모듈 사용

https://velog.io/@gillog/Python-Stack-Queue-기본-module-사용-정리
'''
import queue
q = queue.Queue(5) # 크기 5의 큐 객체 생성
num = 10
while not q.full(): # 큐가 꽉 찰 때까지 10~50 삽입
    q.put(num) # enqueue
    num+=10

print('삭제 순서:', end=' ')
while not q.empty(): # 큐가 비어 있을 때까지 삭제
    num = q.get() # 큐에서 삭제하면서 꺼내옴. dequeue
    print(num, end=' ')
print()

###############################################
from collections import deque
d = deque() # 덱 객체 생성

# addRear(), deleteRear(): append, pop()
# addFront(), deleteFront(): appendleft(), popleft()

for i in range(0, 10): # 덱에 홀수는 앞(왼쪽)에서 짝수는 뒤(오른쪽)에서 삽입하기
    if i%2==1: d.appendleft(i) # 1 3 5 7 9
    else: d.append(i) # 0 2 4 6 8
print('\n결과:', d)

# 앞에서 삭제 2번, 뒤에서 삭제 3번
for i in range(2): d.popleft()
for i in range(3): d.pop()
print('삭제후:', d)

# 앞에 10~13 삽입
for i in range(10, 14): d.appendleft(i)
print('삽입후:', d)