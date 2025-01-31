'''
# 트리
나무~가지. 계층적인 관계를 가진 자료
노드, 에지, 루트
트리는 순환적으로 정의되는 자료구조. 순환 알고리즘이 흔히 사용됨

# 일반 트리
자식의 개수에 제한이 없는 트리를 일반 트리라고 한다.
N-링크: 노드가 N개의 링크를 갖도록 허용하는 것
노드마다 링크의 개수가 다르다는 문제 => 트리의 표현과 관리가 복잡해짐
따라서 실제로는 트리 노드의 자식 수에 제한을 둔다. 2개, 3개

# 이진 트리(binary tree)
모든 노드가 최대 2개의 자식만을 가질 수 있는 트리
부모 노드와 두 개의 서브트리(왼쪽자식과 오른쪽자식)
확장 사례) 이진 탐색 알고리즘 트리, 힙 트리, 수식 트리
종류: 포화 이진트리, 완전 이진트리, 균형 이진트리

# 이진 트리의 표현
1) 배열구조 표현
2) 이중연결리스트 표현

# 이진 트리의 표준순회
순회(traversal): 모든 노드를 한 번씩 방문
  V
 / \
L   R
전위순회: VLR
중위순회: LVR
후위순회: LRV

'''
# 일반 트리
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None        # 왼쪽 자식을 위한 링크
        self.right = None      # 오른쪽 자식을 위한 링크

def preorder(n): # 전위순회(루트-왼-오)
    if n is not None: # 노드가 있을 때까지 순환 호출
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n): # 중위순회(왼-루트-오)
    if n is not None: # 노드가 있을 때까지 순환 호출
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n): # 후위순회(왼-오-루트)
    if n is not None: # 노드가 있을 때까지 순환 호출
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 트리 삽입 129pg
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

# 노드 연결
a.left, a.right = b, c
b.left, b.right = d, e
c.left = f
root = a

# 전위순회 130pg
print('전위 순회:', end=' ')
preorder(root) # 루트부터 탐색 알고리즘 시작
print()

print('중위 순회:', end=' ')
inorder(root) # 루트부터 탐색 알고리즘 시작
print()

print('후위 순회:', end=' ')
postorder(root) # 루트부터 탐색 알고리즘 시작

