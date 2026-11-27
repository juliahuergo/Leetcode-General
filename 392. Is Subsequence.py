class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pts = ptt = 0

        while ptt < len(t) and pts < len(s):
            if t[ptt] == s[pts]:
                ptt += 1
                pts += 1
            else:
                ptt += 1

        return pts == len(s)
