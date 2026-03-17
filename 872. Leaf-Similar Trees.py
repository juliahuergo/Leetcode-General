# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def sequence(ans, root):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                ans.append(root.val)
                return ans
            
            
            sequence(ans, root.left)
            sequence(ans, root.right)

            return ans
        
        seq1 = sequence([], root1)
        seq2 = sequence([], root2)
        if len(seq1) != len(seq2):
            return False

        for leaf1, leaf2 in zip(seq1, seq2):
            if leaf1 != leaf2: 
                return False
        
        return True  

