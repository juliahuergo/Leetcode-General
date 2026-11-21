class StockPrice:

    def __init__(self):
        self.dates = {}
        self.latest = 0
        self.maxPrices = []
        self.minPrices = []

    def update(self, timestamp: int, price: int) -> None:

        self.latest = max(self.latest, timestamp)
        self.dates[timestamp] = price
        heapq.heappush(self.maxPrices, (-price, timestamp))
        heapq.heappush(self.minPrices, (price, timestamp))

    def current(self) -> int:
        return self.dates[self.latest]

    def maximum(self) -> int:
        price, timestamp = self.maxPrices[0]
        
        while self.dates[timestamp] != -price:
            heapq.heappop(self.maxPrices)
            price, timestamp = self.maxPrices[0]
        return -price

    def minimum(self) -> int:
        price, timestamp = self.minPrices[0]
        while self.dates[timestamp] != price:
            heapq.heappop(self.minPrices)
            price, timestamp = self.minPrices[0]
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
