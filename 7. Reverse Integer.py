class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strX = str(x)
        ans = deque()
        for i in range(len(strX)-1, -1, -1):
            if not ans and strX[i] == '0' and len(strX) > 1:
                continue
            elif strX[i] == '-':
                ans.appendleft('-')
            else:   
                ans.append(strX[i])
        
        
        ans = int("".join(ans))
        return ans if ans >= -2**31 and ans <= 2**31 else 0
