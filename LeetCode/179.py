# 179. Largest Number
# Medium

# 4526

# 392

# Add to List

# Share
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109
class Solution:
    @staticmethod
    def to_swap(n1: int, n2:int)->bool:
        return str(n1)+str(n2)<str(n2)+str(n1)
    def largestNumber(self, nums: List[int]) -> str:
        i=1
        while i<len(nums):
            j=i
            while j>0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1]=nums[j-1], nums[j]
                j-=1
            i+=1
        return str(int(''.join(map(str, nums))))
