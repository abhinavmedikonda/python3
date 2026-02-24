from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.dp = [0]
        [self.dp.append(self.dp[-1]+v) for v in nums]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1]-self.dp[left]

if __name__ == '__main__':
    o = NumArray([-2,0,3,-5,2,-1])
    print(o.sumRange(0,2))
    print(o.sumRange(2,5))
    print(o.sumRange(0,5))
