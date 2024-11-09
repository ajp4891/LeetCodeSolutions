class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = 0
        n -= 1

        binx = [0] * 64
        binn = [0] * 64

        for i in range(64):
            bit = (x >> i) & 1
            binx[i] = bit

            bit = (n >> i) & 1
            binn[i] = bit

        posx = 0
        posn = 0

        while posx < 63:
            while binx[posx] != 0 and posx < 63:
                posx += 1

            binx[posx] = binn[posn]
            posx += 1
            posn += 1

        for i in range(64):
            if binx[i] == 1:
                result += pow(2, i)

        return result