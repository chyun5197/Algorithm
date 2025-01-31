class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    # 삽입, 삭제 시에만 연결 링크 양쪽으로 추가
    def insert(self, n, data): # 3
        '''n번째 노드에 해당 데이터를 삽입하는 함수'''
        node = DNode(data)  # 삽입할 노드 생성
        if n == 1:  # 삽일할 위치가 맨 앞일때
            # 기존: head -> m
            # 삽입후: head -> node <=> m
            node.next = self.head # node -> m : 삽일할 노드(node)가 기존의 헤드노드(m)를 가리키도록 변경
            node.next.prev = node # node <- m : 다음 노드(m)의 이전 노드를 삽입할 노드(node)로 가리킴
            self.head = node # head -> node : 삽일할 노드를 헤드 노드로 변경
        else: # 삽입이 맨 앞이 아닐때
            before = self.head  # 삽입할 위치 이전 노드 선언
            for i in range(n-2):  # 삽입할 위치 이전 노드까지 이동
                before = before.next

            # 기존: k(before) <=> p
            # 삽입후: k(before) <=> node <=> p
            node.next = before.next  # node -> p : 삽입할 링크가 다음 노드를 가리킴 2) 맨끝 삽입이면 node->None
            node.prev = before # k <- node : 삽입할 노드가 이전 노드를 가리킴
            if before.next is not None : # 1) 삽입할 위치가 맨 끝이 아니면
                node.next.prev = node
                # node <- p : 다음 노드(p)의 이전 노드를 삽입할 노드(node)로 가리킴
            before.next = node  # k -> node : 전 링크가 삽입할 노드를 가리킴

            # 2) 맨 끝에 삽입할 경우
            # if문 미실행, node <- p 미실행
            # 기존: k(before) -> None
            # 삽입후: k(before) <=> node -> None

    def delete(self, n): # 4
        '''n번째 노드를 삭제하는 함수'''
        if n==1: # 삭제할 위치가 맨 앞일때
            self.head = self.head.next # 다음 링크의 노드를 헤드노드로 변경
        else: # 삭제가 맨 앞이 아닐때
            before = self.head  # 삭제할 위치 이전 노드 선언

            # k(before) <=> d <=> p
            # k(before) <=> p
            for i in range(n-2): # 삭제할 위치 이전 노드까지 이동
                before = before.next # before는 삭제할 위치 이전 노드
            before.next = before.next.next # k -> p : 이전 노드의 링크를 다음 다음 노드로 연결 @ d를 건너뜀
            if before.next is not None : # 1) 삭제할 위치가 맨 끝이 아니면
                before.next.prev = before # k <- p

            # 2) 맨끝 삭제일 경우
            # if문 미실행, k <- p 미실행
            # 기존: k <=> d -> None
            # 삽입후: k(before) -> None


    # size()와 showList()는 동일
    def size(self): # 1
        '''연결된 전체 노드 개수 출력'''
        ptr = self.head
        cnt = 0
        while ptr is not None:
            ptr = ptr.next
            cnt += 1
        return cnt

    def showList(self, ment=''): # 2
        '''모든 이중리스트 출력'''
        print(ment, end='')
        ptr = self.head
        while ptr is not None: # for size()로 해도 됨
            print(f'{ptr.data}<=>', end='')
            ptr = ptr.next
        print('None')

# 노드와 데이터 할당
# 위치   1   2   3   4   5
# 변수   h   a   b   c   t
# 데이터 12  25  9   34  17
h = DNode(12) # 헤드노드
a = DNode(25)
b = DNode(9)
c = DNode(34)
t = DNode(17) # 테일노드

# 모든 노드의 링크를 양옆 이중으로 연결
# h<=>a<=>b<=>c<=>t->None
h.next = a
a.prev, a.next = h, b # h<-a->b
b.prev, b.next = a, c
c.prev, c.next = b, t
t.prev = c

# 이중 연결리스트 설정
# head->h<=>a<=>b<=>c<=>t->None
s = DLinkedList()
s.head = h # head -> h : 연결리스트의 헤드노드를 h노드로 연결
# (head는 링크뿐임, 노드 없음 head<=>h가 아님)

# 노드 개수와 전체 리스트 확인
print('노드 개수:', s.size())
s.showList()
print('='*50)

# 노드 삽입
s.insert(3, 100) # 중간 삽입
s.showList('삽입(3,100): ')
s.insert(1, 200) # 맨앞 삽입
s.showList()
s.insert(s.size()+1, 300) # 맨끝삽입
s.showList()
print('='*50)

# 노드 삭제
s.delete(3) # 중간 삭제
s.showList()
s.delete(1) # 맨 앞 삭제
s.showList()
s.delete(s.size()) # 맨 끝 삭제
s.showList()