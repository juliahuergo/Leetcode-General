# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder_dfs(root, vals):
            if not root:
                return
            inorder_dfs(root.left, vals)
            vals.append(root.val)
            inorder_dfs(root.right, vals)

        
        vals1 = []
        vals2 = []
        inorder_dfs(root1, vals1)
        inorder_dfs(root2, vals2)

        ans = []
        ptr1 = ptr2 = 0
        while ptr1 < len(vals1) and ptr2 < len(vals2):
            if vals1[ptr1] > vals2[ptr2]:
                ans.append(vals2[ptr2])
                ptr2 += 1
            else:
                ans.append(vals1[ptr1])
                ptr1 += 1
        
        while ptr1 < len(vals1):
            ans.append(vals1[ptr1])
            ptr1 += 1
        
        while ptr2 < len(vals2):
            ans.append(vals2[ptr2])
            ptr2 += 1
        
        return ans 
