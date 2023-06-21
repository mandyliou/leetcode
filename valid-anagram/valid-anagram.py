class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0) #gets current count of the char, 0 if not yet present; will add 1 to the retrieved count
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict
        
