# FIFO(First In First Out, 선입선출)
# 가장 먼저 넣은 데이터를 우선적으로 꺼낸다.

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
            print("가득 찼습니다.")
        else:
            self.que.append(value) # 맨 앞에 넣고.. 반대로도 가능

    def dequeue(self):
        '''큐에서 맨 앞 데이터 꺼내기'''
        if self.is_empty():
            print("비어 있습니다.")
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
