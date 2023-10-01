# leetcode 121

class Solution:
    def maxProfit(self, prices):

        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            current_profit = prices[right] - prices[left]
            if current_profit > max_profit:
                max_profit = current_profit

            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit


my_sol = Solution()
print(my_sol.maxProfit([7, 1, 5, 3, 6, 4]))
