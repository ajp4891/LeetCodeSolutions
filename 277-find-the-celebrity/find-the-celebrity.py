# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        q = deque()
        celeb = 0
        for i in range(1, n):
            
            if knows(celeb, i):
                celeb = i

        for j in range(n):
            if celeb == j:
                continue
            if knows(celeb, j) or not knows(j, celeb):
                return -1
            
        return celeb