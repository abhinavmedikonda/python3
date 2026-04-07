class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        outp = [intervals[0]]
        for i in range(1, len(intervals)):
            if outp[-1][1] >= intervals[i][0]:
                outp[-1][1] = max(outp[-1][1], intervals[i][1])
            else:
                outp.append(intervals[i])
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(o.merge([[1,4],[4,5]]))
    print(o.merge([[4,7],[1,4]]
))
