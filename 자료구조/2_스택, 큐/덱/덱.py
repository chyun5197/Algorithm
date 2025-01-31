from Que import *

class Deque(Queue): # 기존 큐 클래스를 상속 받아 덱 구

    # 동일한 함수 상속
    def addRear(self, value): self.enqueue(value)
    def deleteFront(self): self.dequeue()

    # 양방향 함수 추가
    def addFront(self, value):
        if self.is_full():
            print("가득 찼습니다.")
        else:
            self.que.insert(0, value)  # 맨 앞에 넣고.. 반대로도 가능

    def deleteRear(self):
        if self.is_empty():
            print("비어 있습니다.")
        else:
            del self.que[-1]  # 데이터 삭제


dq = Deque(10) # 10개 크기 덱 객체 생성
for i in range(0, 10): # 덱에 홀수는 앞에서 짝수는 뒤에서 삽입하기
    if i%2==1: dq.addFront(i) # 1 3 5 7 9
    else: dq.addRear(i) # 0 2 4 6 8
    print(f'원소{i} 삽입: {dq.get_queue()}')

# [9, 7, 5, 3, 1 | 0, 2, 4, 6, 8]
print('\n결과:', dq.get_queue())

# 앞에서 삭제 2번, 뒤에서 삭제 3번
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
print('삭제후:', dq.get_queue())

# 앞에 10~13 삽입
for i in range(10, 14): dq.addFront(i)
print('삽입후:', dq.get_queue())