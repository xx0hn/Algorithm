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
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31-i])
            B = int(b_bin[31-i])
            
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3
            
            result.append(str(sum))
        if carry == 1:
            result.append('1')
        result = int(''.join(result[::-1]), 2) & MASK
        if result > INT_MAX:
            result = ~(result ^ MASK)
        return result
