# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 0:
            return None
                 
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        #idx is the index of the root in inorder array
        idx = 0
        while inorder[idx] != root.val: 
            idx += 1
        
        leftTree = self.buildTree(preorder[1:idx+1], inorder[:idx])
        rightTree = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        
        return TreeNode(root.val, leftTree, rightTree)
        
