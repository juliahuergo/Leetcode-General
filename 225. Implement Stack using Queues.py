class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        #self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        elems = []
        while self.queue1:
            elems.append(self.queue1.popleft())
        self.queue1.append(x)
        for elem in elems:
            self.queue1.append(elem)
        #Now the leftmost element of the queue is x

    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.popleft()       
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
