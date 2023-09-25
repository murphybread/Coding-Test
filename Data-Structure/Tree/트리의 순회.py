"""
전위순회(pre-order traverse): 루트 먼저 방문
중위순회(in-order traverse): 왼쪽자식 먼저 후 루트 방문
후위순회(post-order traverse): 오른쪽 자식방문 후 루트 방문

"""


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    print(node.data, end=" ")

    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])

    print(node.data, end=" ")

    if node.right_node != None:
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])

    if node.right_node != None:
        post_order(tree[node.right_node])

    print(node.data, end=" ")


n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)


print(tree["A"], tree["A"].data, tree["A"].left_node, tree["A"].right_node)
print("--------------------")
pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
