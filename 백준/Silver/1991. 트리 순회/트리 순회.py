# 입력부
N = int(input())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = (node, left, right)

preResult, inResult, postResult = '', '', ''

# preorder
def preorder(current):
    global preResult
    node, left, right = tree[current]
    if node != '.': preResult += node
    if left != '.': preorder(left)
    if right != '.': preorder(right)

# inorder
def inorder(current):
    global inResult
    node, left, right = tree[current]
    if left != '.': inorder(left)
    if node != '.': inResult += node
    if right != '.': inorder(right)

# postorder
def postorder(current):
    global postResult
    node, left, right = tree[current]
    if left != '.': postorder(left)
    if right != '.': postorder(right)
    if node != '.': postResult += node

# 출력부
preorder('A')
inorder('A')
postorder('A')
print(preResult)
print(inResult)
print(postResult)