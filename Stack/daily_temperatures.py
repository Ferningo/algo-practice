class Solution:
    def dailyTemperatures(self, temperatures):
        temp_stack = []  # (temp,indice)
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]

            if temp_stack:

                # si la temp es menor, agregala al stack
                if temp_stack[-1][0] < temp:

                    current_temp = temp_stack.pop()
                    while current_temp[0] < temp:
                        days = i - current_temp[1]
                        result[current_temp[1]] = days
                        if len(temp_stack) > 0 and temp_stack[-1][0] < temp:
                            current_temp = temp_stack.pop()
                        else:
                            break
                    temp_stack.append([temp, i])

            temp_stack.append([temp, i])

        return result


# my_sol = Solution()
# print(my_sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
