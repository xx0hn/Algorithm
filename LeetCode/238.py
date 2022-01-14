# 238. Product of Array Except Self
# Medium

# 10601

# 667

# Add to List

# Share
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p=1
        for i in range(0, len(nums)):
            out.append(p)
            p=p*nums[i]
        p=1
        for i in range(len(nums)-1, 0-1, -1):
            out[i]=out[i]*p
            p=p*nums[i]
        return out
