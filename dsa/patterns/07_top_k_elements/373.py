import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        mnhp = [(0, 0, 0)]
        vstd = set((0, 0))
        outp = []
        while mnhp and len(outp) < k:
            mn = heapq.heappop(mnhp)
            outp.append([nums1[mn[1]], nums2[mn[2]]])
            if mn[1]+1 < len(nums1) and (mn[1]+1, mn[2]) not in vstd:
                heapq.heappush(mnhp, (nums1[mn[1]+1]+nums2[mn[2]], mn[1]+1, mn[2]))
                vstd.add((mn[1]+1, mn[2]))
            if mn[2]+1 < len(nums2) and (mn[1], mn[2]+1) not in vstd:
                heapq.heappush(mnhp, (nums1[mn[1]]+nums2[mn[2]+1], mn[1], mn[2]+1))
                vstd.add((mn[1], mn[2]+1))
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.kSmallestPairs([1,7,11], [2,4,6], 3))
    print(o.kSmallestPairs([1,1,2], [1,2,3], 2))
    print(o.kSmallestPairs([0,0,0,0,0], [-3,22,35,56,76], 22))
