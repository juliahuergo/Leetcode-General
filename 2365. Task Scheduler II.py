class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        
        hash_map = {} #last day that type was executed

        cont = 0
        for i in range(len(tasks)):
            curType = tasks[i]
            if curType not in hash_map or cont - hash_map[curType] >= space:
                cont += 1
            else:
                cont += (space - (cont - hash_map[curType])) + 1
            
            hash_map[curType] = cont
        
        return cont
                
