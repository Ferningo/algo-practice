# Leetcode 56. Merge Intervals

class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        start = 0
        while start < len(intervals):
            interval, counter = self.helper(start, intervals[start], intervals)
            start += counter
            result.append(interval)
        return result

    def helper(self, start, my_list, list_array):
        result = [my_list[0], my_list[1]]
        counter = 0
        for i in range(start, len(list_array)):
            list_2 = list_array[i]
            if my_list[1] >= list_2[0]:
                result[1] = max(my_list[1], list_2[1])
                my_list = result
                counter += 1
            else:
                break
        return result, counter


# my_sol = Solution()
# print(my_sol.merge([[1, 4], [0, 2], [3, 5]]))
