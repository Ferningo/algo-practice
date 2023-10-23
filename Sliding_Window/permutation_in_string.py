# Leetcode 567
# Permutation in String


class Solution:
    def checkInclusion(self, s1, s2):
        s1_sorted = sorted(s1)
        left = 0
        right = len(s1)

        while right <= len(s2):

            current_string = s2[left:right]
            current_sorted = sorted(current_string)

            if current_sorted == s1_sorted:
                return True

            left += 1
            right += 1

        return False

    def validateDictionary(self, dictionary):
        total_count = 0
        for key in dictionary:
            total_count += dictionary[key]
        return total_count == 0


my_sol = Solution()
print(my_sol.checkInclusion("ab", "eidboaoo"))
