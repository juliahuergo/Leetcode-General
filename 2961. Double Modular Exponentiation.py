class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        cont = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]

            if pow((pow(a, b) %10), c) % m == target:
                cont.append(i)
        
        return cont
