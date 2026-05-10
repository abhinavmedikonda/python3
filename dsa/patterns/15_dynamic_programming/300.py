class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        da = [1] * len(nums)
        for r in range(len(nums)):
            for l in range(r):
                if nums[r] > nums[l]:
                    da[r] = max(da[r], da[l]+1)
        return max(da)
                
if __name__ == '__main__':
    o = Solution()
    print(o.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(o.lengthOfLIS([0,1,0,3,2,3]))
    print(o.lengthOfLIS([7,7,7,7,7,7,7]))
