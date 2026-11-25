# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = [[root.val]]
        level = 0
        while queue:
            add_to_queue = []
            level += 1
            while queue:
                curr = queue.popleft()
                if curr.left:
                    add_to_queue.append(curr.left)
                    if level >= len(ans):
                        ans.append([])
                    ans[level].append(curr.left.val)
                if curr.right:
                    add_to_queue.append(curr.right)
                    if level >= len(ans):
                        ans.append([])
                    ans[level].append(curr.right.val)
            for node in add_to_queue:
                queue.append(node)
        
        return ans 
