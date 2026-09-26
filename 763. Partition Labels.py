class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        last = {}

        for i in range(-1, -len(s)-1, -1):
            if s[i] not in last:
                last[s[i]] = len(s) + i

        ans = []

        i = 0
        
        while i < len(s): #each iteration makes for 1 partition
        
            maximum_aux = last[s[i]]
            
            j = i
            while j <= maximum_aux :
                maximum_aux = max(maximum_aux, last[s[j]])
                j += 1
            
            ans.append(maximum_aux - i + 1)

            i = maximum_aux + 1
        
        return ans 
