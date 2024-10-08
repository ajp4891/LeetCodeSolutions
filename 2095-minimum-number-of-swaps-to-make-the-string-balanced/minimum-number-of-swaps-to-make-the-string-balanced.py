class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        for c in s:
            if c == '[':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
        
        return (cnt + 1) // 2
        