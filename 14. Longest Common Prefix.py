class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        cont = 0
        prefix = ""
        maximum = min(len(word) for word in strs)
        while cont < maximum:
            letter = strs[0][cont]
            for i in range(1, len(strs)):
                if strs[i][cont] != letter:
                    return prefix
            cont += 1
            prefix += letter
        

        return prefix

