# Leetcode 704. Binary Search

class Solution:
    def search(self, array, target):
        left = 0
        right = len(array)

        while left <= right:
            middle = (left + right) // 2
            current = array[middle]

            if current < target:
                left += middle

            elif current > target:
                right = middle - 1

            elif current == target:
                return middle

        return -1


my_sol = Solution()
print(my_sol.search([-1, 0, 3, 5, 9, 12, 13], 13))
