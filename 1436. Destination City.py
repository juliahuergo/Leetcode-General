class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        outgoing = set()
        for path in paths:
            outgoing.add(path[0])
        
        for path in paths:
            if path[1] not in outgoing:
                return path[1]
