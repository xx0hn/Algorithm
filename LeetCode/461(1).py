# 461. Hamming Distance
# Easy

# 2967

# 197

# Add to List

# Share
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=x^y
        return bin(result).count('1')
