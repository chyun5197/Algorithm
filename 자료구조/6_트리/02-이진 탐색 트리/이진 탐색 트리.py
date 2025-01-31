'''
# 이진 탐색 알고리즘 트리(BST: Binary Search Tree)
이진 탐색을 위한 트리
이진 탐색의 성능은 유지하면서 데이터의 삽입과 삭제도 효율적으로 처리하는 트리이다.

# 이진 탐색의 조건
왼쪽 자식노드는 부모 노드보다 작고 오른쪽 자식노드는 부모 노드보다 크다.(좌우 반대 대소도 동일)
(일반적으로 키값 중복 허용X)
'''
class Node:
    def __init__(self, key, value):
        self.key = key # 탐색을 위한 키
        self.value = value # 값
        self.left = None # 왼쪽 자식에 대한 링크
        self.right = None # 오른쪽 자식에 대한 링크

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 키값으로 노드를 검색하는 함수
    def search_key(self, key): # p를 루트 노드로 갖는 이진검색트리에서 키값이 key인 노드 찾기
        p = self.root
        while True:
            if p is None: # 찾는 노드가 없으면
                return None # 검색 실패
            elif key == p.key: # key와 노드p의 keyrk 같으면
                return p # 해당 노드 리턴. 검색 성공
            elif key < p.key: # 찾는게 현재 키보다 더 작으면 왼쪽 서브트리 탐색 알고리즘
                p = p.left
                # return search_key(p.left, key)
            else: # key > p.key. 더 큰 키일때 오른쪽 서브트리 탐색 알고리즘
                p = p.right
                # return search_key(p.right, key)

    # 노드를 삽입하는 함수
    def add(self, key, value):
        def add_node(node, key, value):
            if key == node.key:
                return False # key가 이진 검색 트리에 이미 존재, 삽입 실패
            elif key < node.key:
                if node.left is None: # 왼쪽 서브 노드가 비어 있으면 삽입
                    node.left = Node(key, value)
                else: # 왼쪽 서브 노드가 들어 있으면
                    add_node(node.left, key, value) # 왼쪽 서브노드의 서브 노드들에 대한 탐색 알고리즘 진행
            else: # key > node.key
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    add_node(node.right, key, value)
            return True # 삽입 성공

        if self.root is None: # 트리가 비어있을 경우
            self.root = Node(key, value) # 루트에 삽입
            return True # 삽입 성공
        else: # 트리가 비어있지 않을 경우
            return add_node(self.root, key, value) # 루트의 서브트리부터 삽일할 위치 탐색 알고리즘 시작

    # 노드를 삭제하는 함수
    def remove(self, key):
        p = self.root # 스캔 중인 노드
        parent = None # 스캔 중인 노드의 부모 노드
        is_left_child = True # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            pass
    # 이진 탐색 알고리즘 트리의 노드 삽입 연산
    # def add(root, node): # root임
    #     if root == None: # 공백 노드에 도달하면 이 위치에 삽입
    #         return node
    #
    #     if node.key == root.key:
    #         return root
    #
    #     if node.key < root.key:
    #         root.left = add(root.left, node)
    #     else:
    #         root.right = add(root.right, node)
    #     return root


# 테스트 프로그램(최신 241pg)
data = {6:'육', 8:'팔', 2:'이', 4:'사', 7:'칠',
        5:'오', 1:'일', 9:'구', 3:'삼', 0:'영'}

bst = BinarySearchTree() # 이진검색트리 객체 생성

for key in data:
    bst.add(key, data[key])

# 이진검색트리에서 data 자료의 키값에 대응되는 value값 찾기
for key in data:
    n = bst.search_key(key)
    print(f'이진검색트리{n.key} : ({n.key}, {n.value})')
# print(bst.search_key(6))
