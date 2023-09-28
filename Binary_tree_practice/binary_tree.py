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


def recursive_DFS(root, myArray):
    if root != None:
        myArray.append(root.data)
        recursive_DFS(root.left, myArray)
        recursive_DFS(root.right, myArray)
    return myArray


def BFS(root):
    queue = []
    result = []
    queue.append(root)
    while len(queue) > 0:
        current = queue.pop()
        result.append(current.data)

        if current.left != None:
            queue.insert(0, current.left)

        if current.right != None:
            queue.insert(0, current.right)

    return result


def tree_includes(root, target):
    if root == None:
        return False

    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


print(BFS(my_tree.root))
