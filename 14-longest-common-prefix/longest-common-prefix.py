class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: # Edge case: If the list is empty, return an empty string.
            return ""
        prefix = min(strs, key=len) # Find the shortest string

        for i, char in enumerate(prefix): # Enumerate thru e/ character in the potential prefix.
            for other in strs:
                if other[i] != char: #if character in curr position's diff than other string,
                    return prefix[:i] #return prefix to curr position

        return prefix #if loop finishes without returning, whole shortest string is common prefix