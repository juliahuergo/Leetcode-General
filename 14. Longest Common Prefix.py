class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        

        if len(strs[0]) < 1 or len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            pre = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return ''.join(strs[0][:i])
                if strs[j][i] != pre:
                    return ''.join(strs[0][:i])
                    
            
        
        return strs[0]
