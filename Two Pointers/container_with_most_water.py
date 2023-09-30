# leetcode -11

class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights) - 1

        base = right - left
        height = min(heights[left], heights[right])
        max_area = base * height

        while left < right:
            base = right - left
            height = min(heights[left], heights[right])

            current_area = base * height
            if current_area > max_area:
                max_area = current_area

            if heights[left] < heights[right]:
                left += 1

            else:
                right += -1

        return max_area


my_sol = Solution()
print(my_sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
