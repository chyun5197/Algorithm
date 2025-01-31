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
            return -1
        else:
            self.stk.pop()

    def get_stack(self): #5
        '''스택 데이터들을 반환'''
        return self.stk

    def is_empty(self): #2
        '''스택이 비어있는지 판단'''
        if len(self.stk) == 0:
            return 1
        else:
            return 0
        # return len(self.stk) == 0

    def is_full(self):
        '''스택이 가득 찼는지 판단'''
        return len(self.stk) >= self.size

# Q) 구현한 스택에서 메뉴를 선택하여 데이터를 삽입, 삭제, 확인 등을 해보자.
print('''명령 선택 
1. 데이터를 입력 받아 스택에 삽입하기
2. 스택 데이터 삭제하기
3. 스택 데이터 전부 출력하기
4. 무한반복 종료하기
==============================''')
s = Stack(10) # 크기 10의 스택 객체 생성
while True:
    menu = int(input('메뉴 선택: '))
    if menu==1:
        x = int(input('삽입할 숫자: '))
        s.push(x)
    elif menu==2:
        s.pop()
        print('삭제되었습니다.')
    elif menu==3:
        print(s.get_stack())
    elif menu==4:
        print('프로그램을 종료합니다.')
        break
    print()
