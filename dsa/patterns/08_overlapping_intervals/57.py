import bisect

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i = bisect.bisect_right(intervals, newInterval[0], key = lambda x: x[0])
        l, r = intervals[:i], intervals[i:]
        if l and l[-1][1] >= newInterval[0]:
            l[-1][1] = max(l[-1][1], newInterval[1])
        else:
            l += [newInterval]
        if r and l[-1][1] >= r[0][0]:
            i = bisect.bisect_right(r, l[-1][1], key = lambda x: x[0])
            r[i-1][0] = l[-1][0]
            r[i-1][1] = max(r[i-1][1], l[-1][1])
            return l[:-1] + r[i-1:]
        return l + r

if __name__ == '__main__':
    o = Solution()
    print(o.insert([[1,3],[6,9]], [2,5]))
    print(o.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
