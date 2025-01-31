data = [
    (12, 'A'),
    (33, 'P'),
    (57, 'M'),
    (69, 'R'),
    (41, 'A'),
    None,
    None,
]

data.insert(1, (20, 'K'))
print(data)
'''
일반 배열은 데이터 삽입이나 삭제함에 따라 데이터를 옮겨야해서 효율적이지 않다.
스택이나 큐에서는 자료들을 일렬로 저장하지만 자료에 대한 접근이 앞뒤만으로 제한되어있음
리스트는 제한이 없는 자유로운 선형 자료구조

== 연결 리스트의 구조 ==
# 노드(node)
데이터, 링크 포함
링크는 다른 노드를 가리키는 변수(다른 노드의 주소를 저장)

# 헤드 포인터(head pointer)
헤드 포인터는 헤드 노드의 주소를 저장하는 변수이다.
head pointer->head node-> -> ->... ->tail node->None
테일 노드를의 링크를 처리하는 방법에 따라 단순 연결이나 원형 연결로 구분된다.

1) 단순 연결리스트 (singly linked list)
2) 이중 연결리스트 (doubly linked list)
3) 원형 연결리스트 (circular lined list)
'''
