# Leetcode 20. Valid Parentheses

class Solution:
    def isValid(self, string):
        parenthesis_dict = {')': '(', ']': '[', '}': '{'}

        if len(string) % 2 != 0:
            return False

        my_stack = []
        for character in string:
            if character in ['(', '[', '{']:
                my_stack.append(character)

            else:
                if len(my_stack) == 0:
                    return False

                parenthesis = my_stack.pop()
                if parenthesis_dict[character] != parenthesis:
                    return False

        return len(my_stack) == 0


my_sol = Solution()
print(my_sol.isValid("()"))
print(my_sol.isValid("()[]{}"))
print(my_sol.isValid("(]"))
