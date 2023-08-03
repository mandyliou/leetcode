class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # A stack to keep track of the numbers
        for token in tokens:  # Iterate through each token in the expression
            if token in ["+", "-", "*", "/"]:  # If the token is an operator
                b = stack.pop()  # Pop the last two numbers from the stack
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)  # Perform addition
                elif token == "-":
                    stack.append(a - b)  # Perform subtraction
                elif token == "*":
                    stack.append(a * b)  # Perform multiplication
                elif token == "/":
                    # Perform division, truncating towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))  # If token's a number, push it onto  stack
        return stack[0]  #  result will be the last value remaining on stack

    
