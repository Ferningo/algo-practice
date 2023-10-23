# Leetcode 155. Min Stack
class MinStack:

    def __init__(self):
        self.min_value_stack = []
        self.stack = []

    def push(self, number) -> None:
        if len(self.min_value_stack) == 0:
            self.min_value_stack.append(number)

        else:
            min_val = min(self.min_value_stack[-1], number)
            self.min_value_stack.append(min_val)

        self.stack.append(number)

    def pop(self):
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_value_stack[-1]


# my_stack = MinStack()

# my_stack.push(1)
# my_stack.push(3)
# my_stack.push(8)
# my_stack.push(-2)
# my_stack.pop()
# print(my_stack.top())


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
