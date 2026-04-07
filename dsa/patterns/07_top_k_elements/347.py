from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cntr = Counter(nums)
        uniq = list(cntr.keys())
        mnhp = [(cntr[it], it) for it in uniq[:k]]
        heapq.heapify(mnhp)
        for it in uniq[k:]:
            if cntr[it] > mnhp[0][0]:
                heapq.heappop(mnhp)
                heapq.heappush(mnhp, (cntr[it], it))
        return [it[1] for it in mnhp]
    
if __name__ == '__main__':
    o = Solution()
    print(o.topKFrequent([1,1,1,2,2,3], 2))
    print(o.topKFrequent([1], 1))
    print(o.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
