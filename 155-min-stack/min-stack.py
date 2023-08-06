class MinStack:

    def __init__(self):
        self.mainStack = [] # The main stack to store all elements
        self.minStack = [] # The stack to keep track of the minimum element

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        
        # If minStack is empty or the new element is less than or equal 
        # to the top of minStack, push it to minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # If the element to be popped is the same as the top of minStack,
        # pop it from minStack
        if self.mainStack[-1] == self.minStack[-1]:
            self.minStack.pop()
        
        # Pop from the main stack
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]# Return the top element of mainStack

    def getMin(self) -> int:
        return self.minStack[-1]# Return top element of minStack, which is the current minimum

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()