# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, lst):
            if not node:
                return
            
            dfs(node.left, lst)
            lst.append(node.val)
            dfs(node.right, lst)
            
            return lst
        
        lst = dfs(root, [])
        
        for i in range(1, len(lst)):
            if lst[i] <= lst[i-1]:
                return False
            
        return True
            
        
        
