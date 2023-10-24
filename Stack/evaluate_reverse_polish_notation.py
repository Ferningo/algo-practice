# Leetcode 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '/':
                    stack.append(int(b/a))
        return stack[0]


# my_sol = Solution()
# print(my_sol.evalRPN(["2", "1", "+", "3", "*"]))  # 9
# print(my_sol.evalRPN(["4", "13", "5", "/", "+"]))  # 6
# print(my_sol.evalRPN(["10", "6", "9", "3", "+", "-11",
#       "*", "/", "*", "17", "+", "5", "+"]))  # 22
