# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        def dfs(node, count, parent, direct):
            if not node:
                return 
            
            if not node.left and not node.right:
                if (count+node.val) < limit: #we delete it
                    if direct == "left": parent.left = None
                    elif direct == "right": parent.right = None
                return 
            
            dfs(node.left, count+node.val, node, "left")
            dfs(node.right, count+node.val, node, "right")
            if not node.left and not node.right:
                if direct == "left": parent.left = None
                elif direct == "right": parent.right = None
                return 
            
        dfs(root, 0, None, None)
        return root if root.left or root.right or root.val >= limit else None
        
        
        
    
    
    
    
    
        
