class Solution:
    def climbStairs(self, n: int) -> int:
        da = [1, 2] + ([0] * (n-2))
        for i in range(2, n):
            da[i] = da[i-1]+da[i-2]
        return da[n-1]
                
if __name__ == '__main__':
    o = Solution()
    print(o.climbStairs(2))
    print(o.climbStairs(3))
    print(o.climbStairs(5))
