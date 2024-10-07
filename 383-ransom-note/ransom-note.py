class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ranc = Counter(ransomNote)
        magc = Counter(magazine)

        for c in ranc:
            if c not in magc or ranc[c] > magc[c]:
                return False

        return True