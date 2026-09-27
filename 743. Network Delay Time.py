class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        distances = [10e9 for i in range(n+1)] #distances[i] = from k to node i
        distances[k] = 0
        adjList = {}
        for origin, target, weight in times:
            if origin in adjList:
                adjList[origin].append((weight, target))
            else:
                adjList[origin] = [(weight, target)]

        pq = []
        heapq.heappush(pq, (0, k)) #peso acumulado, nodo


        while pq:
            d, u = heapq.heappop(pq)

            if d > distances[u]: continue

            if u in adjList:
                for weight, neighbour in adjList[u]:
                    if distances[u] + weight < distances[neighbour]:
                        distances[neighbour] = distances[u] + weight
                        heapq.heappush(pq, (distances[neighbour], neighbour))
        
        return max(distances[1:]) if 10e9 not in distances[1:] else -1 
