class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = nums[i]
            first_half = nums[0:i]
            second_half = nums[i+1:]
            partial_array = first_half + second_half
            oposite = (-1 * target)

            solution = self.twoSum(partial_array, (oposite))
            if solution != None:
                a = solution[0]
                b = solution[1]
                if a + b == oposite:
                    triplets = []
                    triplets.append(target)
                    triplets.append(a)
                    triplets.append(b)
                    triplets.sort()
                    if triplets not in result:
                        result.append(triplets)
        return result

    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]

        return None


# numbers = [1, 2, 3, 4, 5]

# i = 3

# first = numbers[0:i]
# second = numbers[i+1:]

# print(first)
# print(second)

# final = first + second
# print(final)

my_sol = Solution()
print(my_sol.threeSum([-1, 0, 1, 2, -1, -4]))
