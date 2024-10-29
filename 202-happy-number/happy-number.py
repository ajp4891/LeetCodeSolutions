class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()
        calc = 0
        while True:
            calc = 0
            for d in str(n):
                calc += (int(d) ** 2)
            
            if calc == 1:
                return True
            
            if calc in seen:
                break

            seen.add(calc)
            n = calc
        return False