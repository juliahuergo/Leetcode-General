class MedianFinder(object):

    def __init__(self):
        self.top = [] #min-heap
        self.bottom = [] #max-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.bottom and num < -1*self.bottom[0]:
            heapq.heappush(self.bottom, -1*num)

        elif self.top and num > self.top[0]:
            heapq.heappush(self.top, num)

        else: #in between both lists -> we add it to the one that has less elements
            if len(self.top) < len(self.bottom):
                heapq.heappush(self.top, num)
            else:
                heapq.heappush(self.bottom, -1*num)

        #we balance them out if necessary
        if len(self.top) != len(self.bottom):
            if len(self.top) > len(self.bottom) + 1: #top is bigger by more than 1 
                heapq.heappush(self.bottom, -1*self.top[0])
                heapq.heappop(self.top)
            elif len(self.bottom) > len(self.top) + 1:
                heapq.heappush(self.top, -1*self.bottom[0])
                heapq.heappop(self.bottom)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.top) > len(self.bottom):
            return self.top[0]
        elif len(self.bottom) > len(self.top):
            return -1*self.bottom[0]
        else:
            return float(self.top[0] + -1*self.bottom[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
