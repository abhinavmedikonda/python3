import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        mnhp = nums[:k]
        heapq.heapify(mnhp)
        for it in nums[k:]:
            if it > mnhp[0]:
                heapq.heappop(mnhp)
                heapq.heappush(mnhp, it)
        return mnhp[0]

if __name__ == '__main__':
    o = Solution()
    print(o.findKthLargest([3,2,1,5,6,4], 2))
    print(o.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
