class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = "".join(map(str, digits))
        digit = int(string) + 1
        return list(map(int, str(digit)))