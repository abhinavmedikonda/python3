import sys


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        da =[[0] * (len(coins)+1)] + [[sys.maxsize] * (len(coins)+1) for _ in range(amount)]
        for r in range(1, len(da)):
            for c, v in enumerate(coins, start=1):
                upon = 1+da[r-v][c] if v <= r else sys.maxsize
                da[r][c] = min(upon, da[r][c-1])
        return -1 if da[-1][-1] == sys.maxsize else da[-1][-1]
                
if __name__ == '__main__':
    o = Solution()
    print(o.coinChange([1,2,5], 11))
    print(o.coinChange([2], 3))
    print(o.coinChange([1], 0))
