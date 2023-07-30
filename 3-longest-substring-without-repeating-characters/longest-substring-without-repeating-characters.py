class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 
        for i in range(len(s)): #outer loop picks where substring starts
            seen_chars = {} #chars seen in this substring
            for j in range(i, len(s)): #inner loop decides where substring ends
                if s[j] in seen_chars: #if the char's seen already, stop checking this substring
                    break

                # If we haven't seen this character, remember it
                seen_chars[s[j]] = True

                # The length of the current substring is j - i + 1
                # If current string's longer than  max_length, then it's new max_length
                max_length = max(max_length, j - i + 1)

        return max_length
