# 347. Top K Frequent Elements
# Medium

# 7156

# 323

# Add to List

# Share
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs=collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        topk=list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk
