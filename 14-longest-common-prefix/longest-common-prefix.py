class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[-1]

        ln = float('inf')
        for s in strs:
            ln = min(len(s), ln)

        i = 0
        pre = []
        exit = False
        while i < ln:
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    exit = True
            if exit:
                break
            pre.append(strs[0][i])
            i += 1

        return ''.join(pre)