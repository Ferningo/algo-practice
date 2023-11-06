# Leetcode 21. Merge Two Sorted Lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        curr_1 = list1
        curr_2 = list2
        dummy = ListNode()
        tail = dummy

        while curr_1 != None and curr_2 != None:

            if curr_1.val <= curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next

            else:
                tail.next = curr_2
                curr_2 = curr_2.next

            tail = tail.next

        if curr_1 != None:
            tail.next = curr_1

        if curr_2 != None:
            tail.next = curr_2

        return dummy.next

    def printLinkedList(self, head):
        current = head
        result = []

        while current != None:
            result.append(current.val)
            current = current.next

        return result


# node_1 = ListNode(1)
# node_2 = ListNode(2)
# node_3 = ListNode(4)

# node_1.next = node_2
# node_2.next = node_3

# list_1 = node_1


# node_4 = ListNode(1)
# node_5 = ListNode(3)
# node_6 = ListNode(4)

# node_4.next = node_5
# node_5.next = node_6

# list_2 = node_4


# my_sol = Solution()

# merded_list = my_sol.mergeTwoLists(list_1, list_2)

# print(my_sol.printLinkedList(merded_list))
