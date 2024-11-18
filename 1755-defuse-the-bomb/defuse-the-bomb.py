class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        if n == 1:
            return code

        l = 1
        total = 0
        r = 0

        if k < 0:
            k = abs(k)
            l = n - k
            r = n - k - 1
        
        ans = []
        for _ in range(k):
            r = (r + 1) % n
            total += code[r]
        
        print(total)
        for _ in range(n):
            ans.append(total)
            total -= code[l]
            l = (l + 1) % n
            r = (r + 1) % n
            total += code[r]

        return ans