# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1

        while left <= right:

            middle = (left + right) // 2
            current_list = matrix[middle]

            if self.isCandidate(current_list, target):

                if self.binary_search(current_list, target) != -1:
                    return True

            if current_list[len(current_list)-1] > target:
                right = middle - 1

            if current_list[0] < target:
                left = middle + 1

        return False

    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1
        while left <= right:

            middle = (left + right) // 2
            current = array[middle]

            if current > target:
                right = middle - 1

            elif current < target:
                left = middle + 1

            else:
                return True

        return -1

    def isCandidate(self, array, target):
        # 1. check if the last number is greater than target
        # 2. check that the first number is smaller than target
        first = array[0]
        last = array[len(array)-1]
        return first <= target and last >= target


my_sol = Solution()
print(my_sol.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
