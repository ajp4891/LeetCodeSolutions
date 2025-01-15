class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = 0

        target = bin(num2).count('1')
        cnts = 0
        crnt = 31

        while cnts < target:
            if (num1 & (1 << crnt)) or (target - cnts > crnt):
                res |= (1 << crnt)
                cnts += 1

            crnt -= 1

        return res