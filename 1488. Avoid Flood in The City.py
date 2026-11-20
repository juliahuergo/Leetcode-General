class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        ans = [1] * len(rains)
        empties = SortedList()
        last_rains = {}

        for idx, k in enumerate(rains):
            if k == 0:
                empties.add(idx)
            else:
                ans[idx] = -1
                if k in last_rains:
                    #first empty that's bigger than last_rains[k]
                    i = empties.bisect(last_rains[k])
                    if i == len(empties): #no such number
                        return []
                    ans[empties[i]] = k
                    empties.discard(empties[i])
                last_rains[k] = idx
            
        return ans
