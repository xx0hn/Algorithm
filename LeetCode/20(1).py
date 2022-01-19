# 20. Valid Parentheses
# Easy

# 10735

# 442

# Add to List

# Share
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        s_list=list(s)
        while s_list:
            tmp=s_list.pop()
            if tmp==')' or tmp==']' or tmp=='}':
                stack.append(tmp)
            else:
                if not stack:
                    return False
                if tmp=='(':
                    if stack.pop()==')':
                        continue
                    else:
                        return False
                if tmp=='[':
                    if stack.pop()==']':
                        continue
                    else:
                        return False
                if tmp=='{':
                    if stack.pop()=='}':
                        continue
                    else:
                        return False
        if stack:
            return False
        return True
