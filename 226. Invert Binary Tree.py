# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invert(root):
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                return root
            
            aux = root.left
            root.left = root.right
            root.right = aux

            invert(root.left)
            invert(root.right)

            return root
        
        return invert(root)
