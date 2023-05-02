class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')': '(', ']': '[', '}': '{'}

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i in pairs: #if i is closing bracket
                if stack and stack[-1] == pairs[i]: 
                    stack.pop()
                else:
                    return False
            else: #if i is opening bracket, append
                stack.append(i)
        if not stack:
            return True
        return False