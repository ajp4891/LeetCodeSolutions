class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        d = dict()
        @cache
        def helper(i, j, opr):
            if opr > k:
                return False
            elif i >= j:
                return True

            elif (i, j) in d:
                return d[(i, j, opr)]

            elif s[i] != s[j]:
                d[(i, j, opr)] = helper(i + 1, j, opr + 1) or helper(i, j - 1, opr + 1)
                return d[(i, j, opr)]
            else:
                return helper(i + 1, j - 1, opr)


        return helper(0, len(s) - 1, 0)
