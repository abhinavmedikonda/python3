class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def recur(have, left):
            if not left:
                outp.append(have)
                return
            for i, v in enumerate(left):
                recur(have+[v], left[:i]+left[i+1:])
        outp = []
        recur([], nums)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.permute([1,2,3]))
    print(o.permute([0,1]))
    print(o.permute([1]))
