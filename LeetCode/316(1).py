# 316. Remove Duplicate Letters
# Medium

# 3666

# 261

# Add to List

# Share
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix=s[s.index(char):]
            if set(s)==set(suffix):
                return char+self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
