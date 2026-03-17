# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            nodes_in_curr_level = len(queue)
            sum_level = 0
            for _ in range(nodes_in_curr_level):
                node = queue.popleft()
                sum_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(sum_level / nodes_in_curr_level)

        return ans 
