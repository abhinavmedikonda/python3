class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        max_ = 0
        score = 0
        hsh = {0: -1}
        for i, v in enumerate(nums):
            score += v if v else -1
            if score in hsh:
                max_ = max(max_, i-hsh[score])
            else:
                hsh[score] = i
        return max_
                
if __name__ == '__main__':
    o = Solution()
    print(o.findMaxLength([0,1]))
    print(o.findMaxLength([0,1,0]))
    print(o.findMaxLength([0,1,1,1,1,1,0,0,0]))
