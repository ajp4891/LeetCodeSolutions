class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(1, n):
            if len(s) >= k:
                break
            inv = "".join(
                "1" if bit == "0" else "0" for bit in s
            )
            s += "1"
            
            s += inv[::-1]

        return s[k-1]