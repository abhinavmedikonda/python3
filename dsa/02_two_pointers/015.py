class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        bkt = set()
        nums.sort()
        for i, v in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while(l < r):
                sm = v + nums[l] + nums[r]
                if sm == 0:
                    tup = (v, nums[l], nums[r])
                    if tup not in bkt:
                        bkt.add(tup)
                    l += 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
        return [list(it) for it in bkt]

if __name__ == '__main__':
    o = Solution()
    print(o.threeSum([-1,0,1,2,-1,-4]))
    print(o.threeSum([0,1,1]))
    print(o.threeSum([0,0,0]))
