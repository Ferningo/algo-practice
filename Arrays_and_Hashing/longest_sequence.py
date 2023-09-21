class Solution:
    def longestConsecutive(self,nums):
        number_set = set(nums)
        longest_sequence = 1
        for number in nums:
            if number-1 in number_set:
                continue
            else:
                current_sequence_len = self.get_sequence_length(number_set,number)
                if longest_sequence < current_sequence_len:
                    longest_sequence = current_sequence_len
        return longest_sequence


    def get_sequence_length(self,set,number):
        helper = 1
        next_number = number + 1
        while next_number in set:
            helper += 1
            next_number += 1
        return helper



my_sol = Solution()
print(my_sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

