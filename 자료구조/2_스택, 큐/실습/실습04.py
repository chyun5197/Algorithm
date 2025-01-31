# B2164
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


q = Queue(500000)
n = int(input())
for i in range(1, n+1):
    q.enqueue(i)

num = 1 # 숫자 1부터 플레이 시작
while len(q.que)!=1: # 큐에 1개 남을 때까지 진행
   if num%2==1: # 1,3,5.. 홀수일 경우 삭제만
       q.dequeue()
   else: # 짝수는 뒤로 옮기기
       tmp = q.que[0] # 옮길 수(삭제될 수)를 저장
       q.dequeue() # 앞에서 삭제
       q.enqueue(tmp) # 뒤에 옮김
   num+=1
print(q.que[0])