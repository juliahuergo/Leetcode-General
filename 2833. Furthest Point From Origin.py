class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        counts = Counter(moves)
        curr = 0

        for direction in moves:
            if direction == 'L':
                curr -= 1
            elif direction == 'R':
                curr += 1
            elif counts['L'] > counts['R']:
                curr -= 1
            else:
                curr += 1
        
        return abs(curr)
