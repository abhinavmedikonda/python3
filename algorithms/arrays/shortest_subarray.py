from collections import deque
import heapq


class Solution:
    def shortestSubarrayOld(self, nums: list[int], k: int) -> int:
        stak = [(0, -1)]
        outp = float('inf')
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while stak and curr - stak[0][0] >= k:
                outp = min(outp, i-heapq.heappop(stak)[1])
            heapq.heappush(stak, (curr, i))
        return -1 if outp == float('inf') else outp

    def shortestSubarray(self, nums: list[int], k: int) -> int:
        stak = deque([(0, -1)])
        outp = float('inf')
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while stak and curr - stak[0][0] >= k:
                outp = min(outp, i-stak.popleft()[1])
            while stak and curr <= stak[-1][0]:
                stak.pop()
            stak.append((curr, i))
        return -1 if outp == float('inf') else outp

if __name__ == '__main__':
    o = Solution()
    print(o.shortestSubarray([1], 1))
    print(o.shortestSubarray([1,2], 4))
    print(o.shortestSubarray([2,-1,2], 3))
