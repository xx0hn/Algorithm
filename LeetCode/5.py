# 5. Longest Palindromic Substring
# Medium

# 15142

# 891

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
