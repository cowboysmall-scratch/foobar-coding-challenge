

class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0

    def is_leaf(self):
        return not self.left and not self.right

    def child_has_value(self, value):
        return not self.is_leaf() and self.left.value == value or self.right.value == value



def perfect_binary_tree(height):
    r = Node()

    if height == 1:
        return r

    r.left = perfect_binary_tree(height - 1)
    r.right = perfect_binary_tree(height - 1)
    return r



def pre_order(node):
    if node == None:
        return []
    return [node] + pre_order(node.left) + pre_order(node.right)

def in_order(node):
    if node == None:
        return []
    return in_order(node.left) + [node] + in_order(node.right)

def post_order(node):
    if node == None:
        return []
    return post_order(node.left) + post_order(node.right) + [node]



def relabel_nodes_pre(root):
    nodes = pre_order(root)
    for i in range(len(nodes)):
        nodes[i].value = i + 1

def relabel_nodes_in(root):
    nodes = in_order(root)
    for i in range(len(nodes)):
        nodes[i].value = i + 1

def relabel_nodes_post(root):
    nodes = post_order(root)
    for i in range(len(nodes)):
        nodes[i].value = i + 1



def find_parent(node, value):
    if node == None:
        return -1

    if node.value == value:
        return -1

    if node.is_leaf():
        return -1

    if node.child_has_value(value):
        return node.value
    else:
        found = find_parent(node.left, value)
        if found == -1:
            found = find_parent(node.right, value)
        return found



def solution(h, q):
    root  = perfect_binary_tree(h)
    relabel_nodes_post(root)
    return [find_parent(root, n) for n in q]

