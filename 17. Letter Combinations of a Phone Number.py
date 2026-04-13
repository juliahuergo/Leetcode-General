class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapLetters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        ans = []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                ans.append(''.join(curr))
                return 
            
            for letter in mapLetters[int(digits[i])]:
                curr.append(letter)
                backtrack(i+1, curr)
                curr.pop()
        
        backtrack(0, [])
        return ans 
