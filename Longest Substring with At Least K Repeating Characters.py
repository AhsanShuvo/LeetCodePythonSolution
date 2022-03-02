class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        visit =  {}
        for i in range(n):
            if s[i] not in visit:
                visit[s[i]] = 0
            visit[s[i]] += 1
        
        j = 0
        while j < n and visit[s[j]] >= k:
            j += 1
        
        if j >= n:
            return j
        
        resL = self.longestSubstring(s[0:j], k)
        
        while j < n and visit[s[j]] < k:
            j += 1
        
        resR = self.longestSubstring(s[j:], k)
        return max(resL, resR)
