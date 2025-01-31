class Node: # 0 아래 예제 포함
    def __init__(self, data):
        self.data = data # 노드에 담을 데이터
        self.next = None # 현재노드가 가리킬 다음노드 링크(주소)

class LinkedList: # 생성자, 검색(데이터가 몇번노드, 몇번째에 무슨노드&데이터, 삽입, 삭제
    def __init__(self):
        self.head = None # 헤드노드 None인 공백으로 초기화

    def getData(self, n): #1
        '''n번째 노드의 데이터를 반환하는 함수'''
        ptr = self.head # 포인터를 헤드부터 시작
        for i in range(n-1): # 헤드노드부터 시작해서 노드 간에 (n-1)번 이동하여 n번째 노드 도착
            ptr = ptr.next
        return ptr.data # n번째 위치 노드의 데이터를 반환

    def search(self, data): #2
        '''해당 데이터를 가지는 노드가 몇 번째에 있는지 반환하는 함수'''
        ptr = self.head  # 포인터를 헤드부터 시작
        cnt = 1 # 몇 번째인지 탐색할 변수
        while ptr is not None: # 처음부터 끝까지 탐색 알고리즘 (tail->None)
            if ptr.data == data:
                return cnt
                # return 크ptr # 노드를 반환하고 싶을때
            ptr = ptr.next
            cnt +=1
        return -1 # 없으면 -1 반환

    def insert(self, n, data): # 5
        '''n번째 노드에 해당 데이터를 삽입하는 함수'''
        node = Node(data) # 삽입할 노드 생성
        if n==1: # 삽일할 위치가 맨 앞일때
            # 기존: head -> m
            # 삽입후: head -> node -> m
            node.next = self.head # node -> m : 삽일할 노드(node)가 기존의 헤드노드(m)를 가리키도록 변경
            self.head = node # head -> node : 삽일할 노드를 헤드 노드로 변경
        else:
            before = self.head  # 삽입할 위치 이전 노드 선언
            for i in range(n-2): # 삽입할 위치 이전 노드까지 이동
                before = before.next

            # @역시 그림 필요 97p
            # 기존: k -> p
            # 삽입후: k(before) -> node -> p
            node.next = before.next # node->p : 삽입할 링크가 다음 노드를 가리킴
            before.next = node # k->node : 전 링크가 삽입할 노드를 가리킴

    def delete(self, n): # 6
        '''n번째 노드를 삭제하는 함수'''
        if n==1: # 삭제할 위치가 맨 앞일때
            self.head = self.head.next # 다음 링크의 노드를 헤드노드로 변경
        else:
            before = self.head  # 삭제할 위치 이전 노드 선언

            # 삭제전: k     ->      d       ->      p
            #           k.next         k.next.next
            # 삭제후: k(before) -> p
            for i in range(n-2): # 삭제할 위치 이전 노드까지 이동
                before = before.next # before는 삭제할 위치 이전 노드
            before.next = before.next.next # k -> p : 이전 노드의 링크를 다음 다음 노드로 연결 @ d를 건너뜀

    def size(self): # 3
        '''연결된 전체 노드 개수 출력'''
        ptr = self.head
        cnt = 0
        while ptr is not None:
            ptr = ptr.next
            cnt += 1
        return cnt

    def showList(self): # 4
        '''모든 리스트 출력'''
        ptr = self.head
        while ptr is not None: # for size()로 해도 됨
            print(f'{ptr.data}->', end='')
            ptr = ptr.next
        print('None')

    # def isEmpty(self):
    #     return self.head == None
    #
    # def isFull(self):
    #     return False

# 노드와 데이터 할당
# 위치   1   2   3   4   5
# 변수   a   b   c   d   e
# 데이터 12  25  9   34  17
a = Node(12) # 헤드노드
b = Node(25)
c = Node(9)
d = Node(34)
e = Node(17) # 테일노드

# 모든 노드의 링크 연결
# a->b->c->d->e->None
a.next = b
b.next = c
c.next = d
d.next = e

print(a.next.data, ': b노드 데이터')
print(a.next.next.data, ': c노드 데이터')
print(a.next.next.next.data, ': d노드 데이터')
print('='*40)

# 연결리스트로 설정
# head->a->b->c->d->e->None
s = LinkedList()
s.head = a # head->a 연결리스트의 헤드노드를 h노드로 연결

# 1. 3번째 노드의 데이터 가져오기
print(s.getData(3))

# 2. 34가 몇번째 노드에 있는지 탐색하기
print(s.search(34))

# 3. 전체 노드 개수 확인
print('노드 개수:', s.size())

# 4. 전체 노드 출력
s.showList()
print('='*40)

# 5. 2번째 위치에 100 삽입
s.insert(3, 100) # 중간 삽입
s.showList()
s.insert(1, 200) # 맨 앞 삽입
s.showList()
s.insert(s.size()+1, 300) # 맨 끝 삽입
s.showList()
print('='*40)

# 6. 3번째 위치 삭제
s.delete(3) # 중간 삭제
s.showList()
s.delete(1) # 맨 앞 삭제
s.showList()
s.delete(s.size()) # 맨 끝 삭제
s.showList()
