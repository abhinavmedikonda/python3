class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == '__main__':
    o = Solution()
    print(o.findDuplicate([1,3,4,2,2]))
    print(o.findDuplicate([3,1,3,4,2]))
    print(o.findDuplicate([3,3,3,3,3]))