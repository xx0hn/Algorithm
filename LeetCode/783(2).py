# 783. Minimum Distance Between BST Nodes
# Easy

# 1509

# 306

# Add to List

# Share
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev=-sys.maxsize
        result=sys.maxsize
        stack=[]
        node=root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            result=min(result, node.val-prev)
            prev=node.val
            node=node.right
        return result
