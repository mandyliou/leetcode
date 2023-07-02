class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        new = []
        for i in s:
            if i not in vowels:
                new.append(i)
        return ''.join(new)

