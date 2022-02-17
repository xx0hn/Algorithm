# 687. Longest Univalue Path
# Medium

# 2920

# 603

# Add to List

# Share
# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [5,4,5,1,1,5]
# Output: 2
# Example 2:


# Input: root = [1,4,5,4,4,5]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int=0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if node.left and node.left.val == node.val:
                left+=1
            else:
                left=0
            if node.right and node.right.val == node.val:
                right+=1
            else:
                right=0
            self.result = max(self.result, left+right)
            return max(left, right)
        dfs(root)
        return self.result
