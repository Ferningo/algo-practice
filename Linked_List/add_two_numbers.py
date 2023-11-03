# Leetcode 2. Add Two Numbers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        factor = 1
        current_1 = l1
        current_2 = l2
        stack = []
        result = None
        while current_1 != None or current_2 != None:
            result = 0

            if current_1 != None:
                result += current_1.val * factor

            if current_2 != None:
                result += current_2.val * factor

            stack.append(result)

        while stack:
            current_node = stack.pop()

            partial_result_node = ListNode()

            partial_result_node.val = current_node.val

            if current_node.next != None:
                partial_result_node.next = current_node.next

            else:
                result = partial_result_node

        return result

    def createLinkedList(self, my_array):
        node = None
        for i in range(len(my_array)):

            node = ListNode(my_array[i])

            if i == len(my_array) - 1:
                node.next = None

            else:
                node.next = my_array[i]

        return node

    def printLinkedList(self, node):
        current = node
        while current != None:
            print(current.val)
            current = current.next


my_sol = Solution()

my_node = my_sol.createLinkedList([2, 4, 3])

print(my_node.next)
