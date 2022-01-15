# 234. Palindrome Linked List
# Easy

# 7541

# 495

# Add to List

# Share
# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True
