class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        lkup = [0] * len(temperatures)
        stk = []
        for i, v in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < v:
                p = stk.pop()
                lkup[p] = i-p
            stk.append(i)
        return lkup

if __name__ == '__main__':
    o = Solution()
    print(o.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(o.dailyTemperatures([30,40,50,60]))
    print(o.dailyTemperatures([30,60,90]))
