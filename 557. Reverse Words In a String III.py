class Solution(object): 
    def reverseWords(self, s): #O(N) because of the list
        """
        :type s: str
        :rtype: str
        """
        
        i = j = 0
        output = []
        while j < len(s):
            #move j to end of the word
            while j + 1 < len(s) and s[j + 1] != ' ':
                j += 1
            
            #copy word in reverse order
            aux = j
            while aux >= i:
                output.append(s[aux])
                aux -= 1
            if j != len(s) - 1:
                output.append(' ')
            #move to next word
            j += 2
            i = j
        
        return ''.join(output)
