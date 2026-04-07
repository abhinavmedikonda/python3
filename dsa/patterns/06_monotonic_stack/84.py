class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        mx = 0
        stk = [-1]
        for i, v in enumerate(heights):
            while stk[-1] != -1 and heights[stk[-1]] > v:
                p = stk.pop()
                mx = max(mx, (i-stk[-1]-1)*heights[p])
            stk.append(i)
        while stk[-1] != -1:
            p = stk.pop()
            mx = max(mx, (len(heights)-stk[-1]-1)*heights[p])
        return mx

if __name__ == '__main__':
    o = Solution()
    print(o.largestRectangleArea([2,1,5,6,2,3]))
    print(o.largestRectangleArea([2,4]))
