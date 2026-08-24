class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        positive = num >= 0  
        num = abs(num)
        remainders = ""
        
        while num != 0:
            remainders = str(num % 7) + remainders
            num //= 7 
        
        
        if not positive: 
            remainders = "-" + remainders

        return remainders 
