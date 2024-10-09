class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)

        total = 0
        for w in words:
            dtmp = Counter(w)
            exclude = False
            cnt = 0
            for k, v in dtmp.items():
                if k not in d or v > d[k]:
                    exclude = True
                    break
                cnt += v

            if not exclude:
                total += cnt

        return total