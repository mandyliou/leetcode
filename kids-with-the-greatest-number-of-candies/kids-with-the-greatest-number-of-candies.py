class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= most:
                result.append(True)
            else:
                result.append(False)
        return result