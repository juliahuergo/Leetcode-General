class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic = {}
        used = set()
        for i in range(len(s)):
            orig, trans = s[i], t[i]
            if (orig in dic and dic[orig] != trans) or (orig not in dic and trans in used):
                return False 
            elif orig not in dic:
                dic[orig] = trans
                used.add(trans)
        
        return True
