# 371. Sum of Two Integers
# Medium

# 2360

# 3559

# Add to List

# Share
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        while b != 0:
            a, b=(a ^ b) & MASK, ((a & b) << 1) & MASK
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a
