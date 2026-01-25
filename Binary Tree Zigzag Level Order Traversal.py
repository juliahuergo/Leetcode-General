# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        LToR = True
        
        ans = []
        
        queue = deque([root])
        
        while queue:
            nodes_in_level = []
            num_nodes_in_level = len(queue)
            
            for i in range(num_nodes_in_level):
                curr = queue.popleft()
                nodes_in_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if not LToR:
                nodes_in_level.reverse()
                
            ans.append(nodes_in_level)
            
            LToR = not LToR
        
        return ans 
        
            
