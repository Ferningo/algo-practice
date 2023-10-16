class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights)-1

        height = min(heights[left], heights[right])
        length = right - left
        max_area = length * height

        while left < right:

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

            height = min(heights[left], heights[right])
            length = right - left
            current_area = length * height

            if max_area < current_area:
                max_area = current_area

        return max_area


my_sol = Solution()

print(my_sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
