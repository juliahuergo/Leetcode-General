class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        mCounts = Counter(magazine)

        for letter in ransomNote:
            if mCounts[letter] <= 0:
                return False
            mCounts[letter] -= 1
        
        return True
