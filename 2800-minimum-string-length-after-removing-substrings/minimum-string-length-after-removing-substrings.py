class Solution:
    def minLength(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        i, j = 0, 1
        s = list(s)
        while j < len(s):
            if (s[i] == "A" and s[j] == "B") or (s[i] == "C" and s[j] == "D"):
                # print(i, j, s[i], s[j])
                s.pop(j)
                s.pop(i)
                i = i - 1 if i > 0 else 0
                j = j - 1 if j > 1 else 1
                # print(i, j)
            else:
                i += 1
                j += 1

        return len(s)