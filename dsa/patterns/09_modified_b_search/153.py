class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = (l+r)//2
            if nums[m-1] > nums[m]:
                return nums[m]
            if nums[l] > nums[m]:
                r = m-1
            else:
                l = m+1

if __name__ == '__main__':
    o = Solution()
    print(o.findMin([3,4,5,1,2]))
    print(o.findMin([4,5,6,7,0,1,2]))
    print(o.findMin([11,13,15,17]))
