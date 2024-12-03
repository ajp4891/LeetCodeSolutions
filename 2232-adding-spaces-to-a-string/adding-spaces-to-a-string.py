class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        sind = 0
        for i, c in enumerate(s):
            if sind < len(spaces) and spaces[sind] == i:
                ans.append(" ")
                sind += 1
                
                
            ans.append(c)

        return ''.join(ans)