class Node:
    def __init__(self, key):
        self.key = key # 탐색을 위한 키
        self.left = None # 왼쪽 자식에 대한 링크
        self.right = None # 오른쪽 자식에 대한 링크

class BinarySearchTree:

    # 노드를 삽입하는 함수

    def add_node(self, node):
        key = node.key
        if key < node.key:
            if node.left is None: # 왼쪽 서브 노드가 비어 있으면 삽입
                node.left = Node(key)
            else: # 왼쪽 서브 노드가 들어 있으면
                self.add_node(node.left) # 왼쪽 서브노드의 서브 노드들에 대한 탐색 알고리즘 진행
        else: # key > node.key
            if node.right is None:
                node.right = Node(key)
            else:
                self.add_node(node.right)
        return True # 삽입 성공



# 이진트리 후위순회
def postorder(n):
    if n is not None: # 노드가 있을 때까지 순환 호출
        postorder(n.left)
        postorder(n.right)
        print(n.key)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

root = Node(int(input()))
bst = BinarySearchTree()
# root = int(input())
# bst.add(root)
while True:
    try:
        node = Node(int(input()))
        bst.add_node(node)
    except:
        break
postorder(root)