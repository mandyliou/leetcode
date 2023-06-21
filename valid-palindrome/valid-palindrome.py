class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for i in s.lower(): #convert to lowercase
            if i.isalnum(): #check alphanumeric by .isalnum()
                new.append(i)
                
        return new == new[::-1] #return true if new is same reversed

        
        
        