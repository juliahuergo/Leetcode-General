# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        i = 0

        while queue:
            nodes_in_curr_level = len(queue)
            prev = float('-inf') if i % 2 == 0 else float('inf') 

            for _ in range(nodes_in_curr_level):
                node = queue.popleft()
                if i % 2 == 0 and (node.val % 2 == 0 or node.val <= prev):
                    return False
                if i % 2 != 0 and (node.val % 2 != 0 or node.val >= prev): 
                    return False
                
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            i += 1
        
        return True
