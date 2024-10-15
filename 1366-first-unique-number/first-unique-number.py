class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.uniq = {}

        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        while self.q and not self.uniq[self.q[0]]:
            self.q.popleft()
        
        if self.q:
            return self.q[0]
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.uniq:
            self.uniq[value] = True
        else:
            self.uniq[value] = False
        
        if self.uniq[value]:
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)