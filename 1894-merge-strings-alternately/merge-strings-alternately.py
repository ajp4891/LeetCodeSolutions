class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i = 0
        # n = len(word1) + len(word2)

        # ans = [""] * (max(len(word1), len(word2)) * 2)

        # for l in word1:
        #     ans[i] = l
        #     i += 2

        # i = 1
        # for l in word2:
        #     ans[i] = l
        #     i += 2

        # return ''.join(ans)

        i = j = 0
        n1, n2 = len(word1), len(word2)
        res = []

        while i < n1 or j < n2:
            if i < n1:
                res.append(word1[i])
                i += 1
            
            if j < n2:
                res.append(word2[j])
                j += 1

        return ''.join(res)