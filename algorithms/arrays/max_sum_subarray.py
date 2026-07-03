'''
53. Maximum Subarray
kadane's algorithm
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxx = float('-inf')
        summ = 0
        for v in nums:
            summ += v
            if summ > maxx:
                maxx = summ
            if summ < 0:
                summ = 0
        return maxx

if __name__ == '__main__':
    o = Solution()
    print(o.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(o.maxSubArray([1]))
    print(o.maxSubArray([5,4,-1,7,8]))
