class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size==0

    def insert(self, data):
        node = Node(data)
        if self.is_empty(): # 처음 넣을때. n1 -> head -> n1
            node.next = node # 다음 노드가 본인 참조
            self.head = node # head도 자신
        else: # 2개 이상부터. n1 -> n2 -> head -> n1
            node.next = self.head # n2 -> head
            self.head = node # head -> n1
        self.size += 1

    def delete(self):
        pass

    def showList(self):
        if self.is_empty():
            print('비었다')
        else:
            ptr = self.head
            first = ptr
            while ptr.next != first:
                print(f'{ptr.data} ->', end='')
                ptr = ptr.next
            print(ptr.data)

# https://velog.io/@9e0na/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%B4%EC%A4%91-%EC%9B%90%ED%98%95-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8

foods = [3, 1, 2]
f = []
for i in range(3):
    f.append(Node(foods[i]))