class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ver1 = version1.split(".")
        ver2 = version2.split(".")

        for a, b in zip_longest(ver1, ver2, fillvalue = 0):
            a = int(a)
            b = int(b)
            if a < b:
                return -1
            elif a > b:
                return 1
        
        return 0
            
