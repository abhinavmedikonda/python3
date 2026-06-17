'''
115. Distinct Subsequences
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def recur(si, ti):
            if (si, ti) in hmap:
                return hmap[(si, ti)]
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            outp = recur(si+1, ti)
            if s[si] == t[ti]:
                outp += recur(si+1, ti+1)
            hmap[(si, ti)] = outp
            return outp
        hmap = {}
        return recur(0, 0)

if __name__ == '__main__':
    o = Solution()
    print(o.numDistinct('arabbbit', 'arabbit'))
    print(o.numDistinct('babgbag', 'bag'))
