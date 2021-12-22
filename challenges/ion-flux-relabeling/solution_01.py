

class Node:

    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = 0



def perfect_binary_tree(height, parent):
    r = Node()
    r.parent = parent

    if height != 1:
        r.left   = perfect_binary_tree(height - 1, r)
        r.right  = perfect_binary_tree(height - 1, r)

    return r



def post_order(node):
    if node == None:
        return []
    return post_order(node.left) + post_order(node.right) + [node]



def relabel_nodes(root):
    nodes = post_order(root)
    for i in range(len(nodes)):
        nodes[i].value = i + 1



def find_node(node, value):
    if node == None:
        return None

    if node.value == value:
        return node

    return find_node(node.left, value) or find_node(node.right, value)



def solution(h, q):
    root  = perfect_binary_tree(h, None)
    relabel_nodes(root)
    nodes = [find_node(root, n) for n in q]
    return [n.parent.value if n.parent else -1 for n in nodes]

