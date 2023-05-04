class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split()
        return len(new[-1])
