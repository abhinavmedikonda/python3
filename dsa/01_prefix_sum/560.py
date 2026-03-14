class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        out_ = sm = 0
        hsh = {0: 1}
        for v in nums:
            sm += v
            out_ += hsh.get(sm-k, 0)
            hsh[sm] = 1 + hsh.setdefault(sm, 0)
        return out_

if __name__ == '__main__':
    o = Solution()
    print(o.subarraySum([1,1,1], 2))
    print(o.subarraySum([1,2,3], 3))
