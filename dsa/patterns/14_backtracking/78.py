class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def recur(i):
            if i == len(nums):
                outp.append(curr[:])
                return
            curr.append(nums[i])
            recur(i+1)
            curr.pop()
            recur(i+1)
        outp = []
        curr = []
        recur(0)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.subsets([1,2,3]))
    print(o.subsets([0]))
