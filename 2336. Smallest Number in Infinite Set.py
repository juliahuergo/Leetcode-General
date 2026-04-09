class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = range(1, 1001) #at most 1000 calls to popSmallest
        heapq.heapify(self.heap)
        self.nums = set(range(1, 1001))

    def popSmallest(self):
        """
        :rtype: int
        """
        elem = heapq.heappop(self.heap)
        self.nums.remove(elem)
        return elem


    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.nums:
            heapq.heappush(self.heap, num)
            self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
