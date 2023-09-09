class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if characters at specific indices in s1 and s2 can be matched.
        # Using sets ensures order-independent matching.
        return ({s1[0], s1[2]} == {s2[0], s2[2]} and 
                {s1[1], s1[3]} == {s2[1], s2[3]})
