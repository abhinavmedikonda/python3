class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sm = numbers[l] + numbers[r]
            if sm == target:
                return [l+1, r+1]
            elif sm < target:
                l += 1
            else:
                r -= 1

if __name__ == '__main__':
    o = Solution()
    print(o.twoSum([2,7,11,15], 9))
    print(o.twoSum([2,3,4], 6))
    print(o.twoSum([-1,0], -1))
