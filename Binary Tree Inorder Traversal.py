# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        
        def printNodes(node):
            if not node:
                return
            
            printNodes(node.left)
            ans.append(node.val)
            printNodes(node.right)
            
            
        ans = []
        printNodes(root)
        
        return ans 
