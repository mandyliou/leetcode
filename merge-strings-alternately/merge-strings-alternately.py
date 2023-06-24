class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        for w1, w2 in zip(word1, word2):
            res += w1 + w2
        if len(word1) > len(word2):
            res += word1[len(word2):]
        else:
            res += word2[len(word1):]
        return res