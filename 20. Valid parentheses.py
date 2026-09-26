class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        contrary = {
            ')' : '(', '}': '{', ']': '['
        }

        queue = deque([])

        for i in range(len(s)):
            if len(queue) > len(s) - i:
                return False 

            symbol = s[i]
            if queue and symbol in contrary and queue[-1] == contrary[symbol]:
                queue.pop()
            else:
                queue.append(symbol)
        
        return not queue 
