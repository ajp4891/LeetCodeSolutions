class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # d = Counter(chars)

        # total = 0
        # for w in words:
        #     dtmp = Counter(w)
        #     include = True
        #     cnt = 0
        #     for k, v in dtmp.items():
        #         if k not in d or v > d[k]:
        #             include = False
        #             break
        #         cnt += v

        #     if include:
        #         total += cnt

        # return total

        ans = []

        for w in words:
            for c in set(w):
                if chars.count(c) < w.count(c):
                    break
            else:
                ans.append(len(w))

        return sum(ans)