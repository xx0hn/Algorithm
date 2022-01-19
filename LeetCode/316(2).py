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
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char]-=1
            if char in seen:
                continue
            while stack and char<stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
