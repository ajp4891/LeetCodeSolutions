import re
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0

        q = deque([beginWord])

        ans = 1

        while q:
            n = len(q)
            ans += 1

            for _ in range(n):
                word = q.popleft()

                for i in range(len(word)):
                    for j in range(26):
                        tmp = word[:i] + chr(ord('a') + j) + word[i+1:]

                        if tmp == endWord:
                            return ans

                        if tmp in wordset:
                            q.append(tmp)
                            wordset.remove(tmp)

        return 0