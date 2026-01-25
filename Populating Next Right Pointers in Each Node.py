"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            
            num_nodes_in_level = len(queue)
            
            for i in range(num_nodes_in_level):
                curr = queue.popleft()
                if i < num_nodes_in_level - 1: #it is not the rightmost node
                    curr.next = queue[0] #next node on its level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return root
                
            
