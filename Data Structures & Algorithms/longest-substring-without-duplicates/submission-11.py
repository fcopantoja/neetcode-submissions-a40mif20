class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        frequencies = [0] * 128
        l, r = 0, 0
        res = 0

        while r < len(s):
            idx = ord(s[r])
            frequencies[idx] += 1
            
            while frequencies[idx] >= 2:
                frequencies[ord(s[l])] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
