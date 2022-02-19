# 297. Serialize and Deserialize Binary Tree
# Hard

# 6074

# 237

# Add to List

# Share
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue=collections.deque([root])
        result=['#']
        while queue:
            node=queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ''.join(result)
        
    def deserialize(self, data):
        if data=='# #':
            return None
        nodes=data.split()
        root=TreeNode(int(nodes[1]))
        queue=collections.deque([root])
        index=2
        while queue:
            node=queue.popleft()
            if nodes[index] is not '#':
                node.left=TreeNode(int(nodes[index]))
                queue.append(node.left)
            index+=1
            
            if nodes[index] is not '#':
                node.right=TreeNode(int(nodes[index]))
                queue.append(node.right)
            index+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
