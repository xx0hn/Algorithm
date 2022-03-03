# 75. Sort Colors
# Medium

# 8909

# 388

# Add to List

# Share
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue=0, 0, len(nums)
        
        while white<blue:
            if nums[white]<1:
                nums[red], nums[white]=nums[white], nums[red]
                white+=1
                red+=1
            elif nums[white]>1:
                blue-=1
                nums[white], nums[blue]=nums[blue], nums[white]
            else:
                white+=1
