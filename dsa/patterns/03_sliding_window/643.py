class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sm = sum(nums[0:k])
        mx = sm/k
        for i in range(1, len(nums)-k+1):
            sm -= nums[i-1]
            sm += nums[i+k-1]
            mx = max(mx, sm/k)
        return mx

if __name__ == '__main__':
    o = Solution()
    print(o.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(o.findMaxAverage([5], 1))
