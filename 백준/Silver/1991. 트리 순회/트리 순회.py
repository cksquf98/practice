def preOrder(node):
    if(node != '.'):
        print(node, end='')
        preOrder(tree.get(node)[0])
        preOrder(tree.get(node)[1])

def inOrder(node):
    if(node != '.'):
        inOrder(tree.get(node)[0])
        print(node, end='')
        inOrder(tree.get(node)[1])

def postOrder(node):
    if(node != '.'):
        postOrder(tree.get(node)[0])
        postOrder(tree.get(node)[1])
        print(node, end='')

import sys
input = sys.stdin.readline

N = int(input())
tree = {}
root = ''

for i in range(N):
    input_list = list(input().split())
    tree[input_list[0]] = [input_list[1], input_list[2]]
    if(i == 0):
        root = input_list[0]

preOrder(root)
print()
inOrder(root)
print()
postOrder(root)