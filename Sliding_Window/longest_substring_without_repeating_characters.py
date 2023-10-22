# Leetcode 3
# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, string):
        max_length = 0
        left = 0
        charSet = set()

        for i in range(len(string)):
            character = string[i]

            if character not in charSet:
                charSet.add(character)

            else:
                while character in charSet:
                    charSet.remove(string[left])
                    left += 1

            charSet.add(character)

            max_length = max(max_length, len(charSet))

        return max_length


my_sol = Solution()
print(my_sol.lengthOfLongestSubstring("pwwkew"))
