from collections import defaultdict
import sys


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stck = [sys.maxsize]
        hmap = defaultdict(lambda: -1)
        for v in nums2:
            while v > stck[-1]:
                hmap[stck.pop()] = v
            stck.append(v)
        return [hmap[v] for v in nums1]

if __name__ == '__main__':
    o = Solution()
    print(o.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(o.nextGreaterElement([2,4], [1,2,3,4]))
