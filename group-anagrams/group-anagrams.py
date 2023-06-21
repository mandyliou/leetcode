class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #map current count of each string to anagram
        for s in strs: #going thru every string
            count = [0] * 26 #initially will have an array of 26 0's; a...z
            
            for c in s: #going thru all characters in each string
                count[ord(c) - ord('a')] += 1 #increment by 1, count how many char u have
            result[tuple(count)].append(s) #in python, lists cant be keys; change it to tuple
        return result.values() #return grouped anagrams
