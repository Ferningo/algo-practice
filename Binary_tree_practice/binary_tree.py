class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
my_tree = BinaryTree(a)

a.left = b
a.right = c

b.left = d
b.right = e

c.right = f


def DFS(root):
    result = []
    if root != None:
        print("Entre aki")
        my_stack = [root]
        while len(my_stack) != 0:
            my_node = my_stack.pop()

            if my_node.right != None:
                my_stack.append(my_node.right)

            if my_node.left != None:
                my_stack.append(my_node.left)

            result.append(my_node.data)

    return result


print(DFS(my_tree.root))
