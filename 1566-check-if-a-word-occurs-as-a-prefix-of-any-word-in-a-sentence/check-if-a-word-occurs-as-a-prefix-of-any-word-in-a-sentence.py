class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        slen = len(searchWord)
        sentence = sentence.split()
        for i, w in enumerate(sentence):
            if w.startswith(searchWord):
                return i + 1
        return -1