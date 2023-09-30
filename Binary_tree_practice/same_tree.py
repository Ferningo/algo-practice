class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


class Solution:
    def isSameTree(self, p, q) -> bool:
        result_1 = self.DFS(p)
        result_2 = self.DFS(q)
        return result_1 == result_2

    def DFS(self, root):
        result = []
        if root != None:
            my_stack = [root]
            while len(my_stack) != 0:
                my_node = my_stack.pop()

                if my_node.right != None:
                    my_stack.append(my_node.right)

                if my_node.left != None:
                    my_stack.append(my_node.left)

                result.append(my_node.val)

        return result


my_Sol = Solution()
print(my_Sol.DFS(a))
