from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out_ = sm = 0
        hsh = {0: 1}
        for v in nums:
            sm += v
            out_ += hsh.get(sm-k, 0)
            hsh[sm] = 1 + hsh.setdefault(sm, 0)
        return out_

if __name__ == '__main__':
    o = Solution()
    out = o.subarraySum([1,2,3], 3)
    print(out)