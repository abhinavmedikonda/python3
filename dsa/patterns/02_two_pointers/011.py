import sys

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_ = -sys.maxsize
        l, r = 0, len(height)-1
        while(l < r):
            max_ = max(max_, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_

if __name__ == '__main__':
    o = Solution()
    print(o.maxArea([1,8,6,2,5,4,8,3,7]))
    print(o.maxArea([1,1]))
    print(o.maxArea([1,2, 4, 6, 4, 8, 9]))
