class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        hmap = {}
        def recur(l, r):
            if l > r:
                return 0
            if l == r:
                return ns[l-1]*ns[l]*ns[l+1]
            if (l, r) in hmap:
                return hmap[(l, r)]
            mx = 0
            for i in range(l, r+1):
                sm = recur(l, i-1) + ns[l-1]*ns[i]*ns[r+1] + recur(i+1, r)
                mx = max(mx, sm)
            hmap[(l, r)] = mx
            return mx
        ns = [1] + nums + [1]
        return recur(1, len(ns)-2)
                
if __name__ == '__main__':
    o = Solution()
    print(o.maxCoins([3,1,5,8]))
    print(o.maxCoins([1,5]))
