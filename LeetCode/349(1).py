# 349. Intersection of Two Arrays
# Easy

# 2548

# 1857

# Add to List

# Share
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)>len(nums1):
            nums1, nums2=nums2, nums1
        nums1.sort()
        answer=set()
        for i in range(len(nums2)):
            left, right=0, len(nums1)-1
            while left<=right:
                mid=(left+right)//2
                if nums1[mid]<nums2[i]:
                    left=mid+1
                elif nums1[mid]>nums2[i]:
                    right=mid-1
                else:
                    answer.add(nums1[mid])
                    break
        return answer
