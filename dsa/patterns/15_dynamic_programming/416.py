class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sm = sum(nums)
        if sm%2 == 1:
            return False
        trgt = sm/2
        hs = set([0])
        for n in nums:
            temp = set()
            for v in hs:
                if n+v == trgt:
                    return True
                temp.add(n+v)
            hs.update(temp)
        return False
                
if __name__ == '__main__':
    o = Solution()
    print(o.canPartition([1,5,11,5]))
    print(o.canPartition([1,2,3,5]))
