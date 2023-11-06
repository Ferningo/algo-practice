# Leetcode 143. Reorder List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        my_list = []
        current = head
        while current != None:
            my_list.append(current)
            current = current.next

        left = 0
        right = len(my_list) - 1
        current = head
        while left < right:
            helper = current.next
            current.next = my_list[right]
            my_list[right].next = helper
            left += 1
            right -= 1

        return current

    def printLinkedList(self, head):
        current = head
        result = []

        while current != None:
            result.append(current.val)
            current = current.next

        return result


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6


my_sol = Solution()
my_sol.reorderList(node_1)
print(my_sol.printLinkedList(node_1))
