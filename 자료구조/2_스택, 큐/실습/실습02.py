# C1714
# pop 함수 리턴하도록 수정 필요
# 스택 클래스 선언
class Stack:
    def __init__(self, size): #1
        '''스택 초기화'''
        self.stk = [] # 스택 본체
        self.size = size # 스택의 크기 설정

    def __len__(self): #4
        '''스택에 들어 있는 데이터 개수를 반환'''
        return len(self.stk)

    def push(self, value): #3
        '''스택에 데이터입 삽입'''
        if self.is_full():
            print("스택이 가득 찼습니다.")
        else:
            self.stk.append(value)

    def pop(self):
        '''스택에서 마지막(최근) 데이터 꺼내기'''
        if self.is_empty():
            print("스택이 비어 있습니다.")
        else:
            return self.stk.pop()

    def get_stack(self): #5
        '''스택 데이터들을 반환'''
        return self.stk

    def is_empty(self): #2
        '''스택이 비어있는지 판단'''
        return len(self.stk) == 0

    def is_full(self):
        '''스택이 가득 찼는지 판단'''
        return len(self.stk) >= self.size

# 스택 객체 생성
s = Stack(50) # 크기 50의 스택 객체 생성

num = input() # 문자열로 숫자 입력 받음
n = len(num) # 문자열 개수(숫자 자리수)
for i in range(n):
    s.push(num[i])

for i in range(n):
    print(s.pop(), end='')

print()
idx = -1
for i in range(n):
    print(num[idx], end='')
    idx-=1