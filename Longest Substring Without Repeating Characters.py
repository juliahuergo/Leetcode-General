class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        
        seen = []
        
        ans = 0
        
        while right < len(s):
            
            while s[right] in seen and left < right:
                seen.pop(0)
                left += 1
            
            seen.append(s[right])
            
            ans = max(ans, right - left + 1)
            
            
            right += 1
        
        return ans 
                
