class Solution:
    def compressedString(self, word: str) -> str:
        comp  = []
        count = 1
        prev_c = word[0]
        for c in word[1:]:
            if c != prev_c or count == 9:
                comp.append(str(count))
                comp.append(prev_c)
                prev_c = c
                count = 0
            count += 1

        comp.append(str(count))
        comp.append(prev_c)
        return ''.join(comp)