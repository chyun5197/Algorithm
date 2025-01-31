# 큐 클래스 선언
class Queue:
    def __init__(self, size):
        '''큐 초기화'''
        self.que = [] # 큐 본체
        self.size = size # 큐의 크기 설정

    def __len__(self):
        '''큐에 들어 있는 데이터 개수를 반환'''
        return len(self.que)

    def enqueue(self, value):
        '''큐에 데이터 삽입'''
        if self.is_full():
            print("큐가 가득 찼습니다.")
        else:
            self.que.append(value) # 맨 앞에 넣고.. 반대로도 가능

    def dequeue(self):
        '''큐에서 맨 앞 데이터 꺼내기'''
        if self.is_empty():
            print("큐가 비어 있습니다.")
        else:
            del self.que[0] # 데이터 삭제

    def get_queue(self):
        '''큐 데이터들을 반환'''
        return self.que

    def is_empty(self):
        '''큐가 비어있는지 판단'''
        return len(self.que) == 0

    def is_full(self):
        '''큐가 가득 찼는지 판단'''
        return len(self.que) >= self.size

# Q) 구현한 큐에서 메뉴를 선택하여 데이터를 삽입, 삭제, 확인 등을 해보자.
print('''명령 선택 
1. 데이터를 입력 받아 스택에 삽입하기
2. 큐 데이터 삭제하기
3. 큐 데이터 전부 출력하기
4. 무한반복 종료하기
==============================''')

q = Queue(5)
while True:
    menu = int(input('메뉴 선택: '))
    if menu==1:
        x = int(input('삽입할 숫자: '))
        q.enqueue(x)
    elif menu==2:
        q.dequeue()
        print('삭제되었습니다.')
    elif menu==3:
        print(q.get_queue())
    elif menu==4:
        print('프로그램을 종료합니다.')
        break
    print()