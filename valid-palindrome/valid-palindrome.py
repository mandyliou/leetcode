class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum(): #removes punctuations, whitespaces; considers digits 
                new += i.lower() #changes to lower case
        return new == new[::-1] #returns true if palindrome

        
        
        