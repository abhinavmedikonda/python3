from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hsh = defaultdict(lambda: -1)
        stk = []
        for n in nums2:
            while stk and stk[-1]<n:
                hsh[stk.pop()] = n
            stk.append(n)
        return [hsh[n] for n in nums1]

if __name__ == '__main__':
    o = Solution()
    print(o.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(o.nextGreaterElement([2,4], [1,2,3,4]))