class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        mnhp = nums[:k]
        for i in range((k-1)//2, -1, -1):
            self.heapify_down(mnhp, i)
        for i in range(k, len(nums)):
            if nums[i] > mnhp[0]:
                mnhp[0] = nums[i]
                self.heapify_down(mnhp, 0)
        return mnhp[0]
    def heapify_down(self, mnhp, i):
        l = (i*2)+1
        r = (i*2)+2
        mn = i
        if l < len(mnhp) and mnhp[l] < mnhp[mn]:
            mn = l
        if r < len(mnhp) and mnhp[r] < mnhp[mn]:
            mn = r
        if mn != i:
            self.swap(mnhp, i, mn)
            self.heapify_down(mnhp, mn)
    def swap(self, mnhp, a, b):
        temp = mnhp[a]
        mnhp[a] = mnhp[b]
        mnhp[b] = temp


if __name__ == '__main__':
    o = Solution()
    print(o.findKthLargest([3,2,1,5,6,4], 2))
    print(o.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
