# 226. Invert Binary Tree
# Easy

# 7616

# 103

# Add to List

# Share
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=collections.deque([root])
        while q:
            node=q.popleft()
            if node:
                node.left, node.right=node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root
