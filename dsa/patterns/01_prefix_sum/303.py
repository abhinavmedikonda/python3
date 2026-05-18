class Solution:
    def __init__(self, nums: list[int]):
        self.dp = [0]
        for v in nums:
            self.dp.append(self.dp[-1]+v)

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1]-self.dp[left]

if __name__ == '__main__':
    o = Solution([-2,0,3,-5,2,-1])
    print(o.sumRange(0,2))
    print(o.sumRange(2,5))
    print(o.sumRange(0,5))
