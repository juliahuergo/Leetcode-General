class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        extra = ['a', 'b', 'c', 'd', 'e', 'f']

        remainders = ""
        if num < 0:
            num += 2**32

        while num != 0:
            remainder = num % 16
            if remainder > 9:
                remainder = extra[remainder-10]
            remainders = str(remainder) + remainders
            num //= 16
        
        return remainders
        
        

