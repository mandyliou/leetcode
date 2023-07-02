class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set("aeiou")
        nonvowels = []
        for i in s:
            if i not in vowels:
                nonvowels.append(i)
        return ''.join(nonvowels)

