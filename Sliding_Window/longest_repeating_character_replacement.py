# Leetcode 424
# Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, string, k):
        left = 0
        right = 0
        result = 0
        char_dict = {}
        while right < len(string):

            char_dict[string[right]] = 1 + char_dict.get(string[right], 0)

            while (right - left + 1) - max(char_dict.values()) > k:
                char_dict[string[left]] -= 1
                left += 1

            result = max(result, right-left+1)
            right += 1

        return result


my_sol = Solution()
print(my_sol.characterReplacement("AABABBA", 1))
