# 15. 3Sum
# Medium

# 15287

# 1477

# Add to List

# Share
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                if sum < 0:
                    left+=1
                elif sum > 0:
                    right-=1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1            
        return results
