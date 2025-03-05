class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            grouplen = 1
            while i + grouplen < len(chars) and chars[i + grouplen] == chars[i]:
                grouplen += 1

            chars[res] = chars[i]
            res += 1

            if grouplen > 1:
                str_len = str(grouplen)
                chars[res:res+len(str_len)] = list(str_len)
                res += len(str_len)
            i += grouplen

        return res