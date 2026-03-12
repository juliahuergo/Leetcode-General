class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(prices)
        decreasing = deque()

        for i in range(len(prices)):
            while decreasing and prices[decreasing[-1]] >= prices[i]:
                answer[decreasing[-1]] = prices[decreasing[-1]] - prices[i]
                decreasing.pop()
            decreasing.append(i)
        while decreasing:
            answer[decreasing[-1]] = prices[decreasing[-1]]
            decreasing.pop()
            
        return answer
