# LIFO(Last In First Out, 후입선출)
# 가장 마지막(최근)에 넣은 데이터를 우선적으로 꺼낸다.

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
            print("스택이 가득 찼습니다.") #예외처리로 변경?
        else:
            self.stk.append(value)

    def pop(self):
        '''스택에서 마지막(최근) 데이터 꺼내기'''
        if self.is_empty():
            print("스택이 비어 있습니다.")
        else:
            self.stk.pop()
    def get_stack(self): #5
        '''스택 데이터들을 반환'''
        return self.stk

    def is_empty(self): #2
        '''스택이 비어있는지 판단'''
        # if len(self.stk) == 0:
        #     return True
        # else:
        #     return False
        return len(self.stk) == 0

    def is_full(self):
        '''스택이 가득 찼는지 판단'''
        return len(self.stk) >= self.size

# 스택 객체 생성
s = Stack(4) # 크기 4의 스택 객체 s 생성

# 데이터 삽입
s.push(10)
print(s.get_stack())
s.push(20)
print(s.get_stack())
s.push(30)
print(s.get_stack())
s.push(40)
print(s.get_stack())
s.push(50)
print(s.get_stack())
print()

# 데이터 꺼내기
s.pop()
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()

