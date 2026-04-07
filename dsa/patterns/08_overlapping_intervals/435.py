import sys

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        mx = -sys.maxsize
        op = 0
        for it in intervals:
            if mx > it[0]:
                op += 1
            else:
                mx = it[1]
        return op
        

if __name__ == '__main__':
    o = Solution()
    print(o.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(o.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(o.eraseOverlapIntervals([[1,2],[2,3]]))
