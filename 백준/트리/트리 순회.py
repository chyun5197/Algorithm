class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 전위순회
def preorder(n):
    if n is not None: # 노드가 있을 때까지 순환 호출
        print(n.data, end='')
        preorder(n.left)
        preorder(n.right)

# 중위순회
def inorder(n):
    if n is not None: # 노드가 있을 때까지 순환 호출
        inorder(n.left)
        print(n.data, end='')
        inorder(n.right)

# 후위순회
def postorder(n):
    if n is not None: # 노드가 있을 때까지 순환 호출
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

# 0 1 2
# 65 66 67
nodes = [Node(chr(ord('A')+i)) for i in range(n)]
for i in range(n):
    p, l, r = input().split()
    node = nodes[ord(p)-65]
    if l!='.':
        node.left = nodes[ord(l)-65]
    if r!='.':
        node.right = nodes[ord(r)-65]
root = nodes[0]
preorder(root)
print()
inorder(root)
print()
postorder(root)


