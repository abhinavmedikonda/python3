from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mn = ''
        tgt = Counter(t)
        wndo = {}
        have, need = 0, len(tgt)
        l = 0
        for r, v in enumerate(s):
            wndo[s[r]] = wndo.get(s[r], 0) + 1
            if s[r] in tgt and wndo[s[r]] == tgt[s[r]]:
                have += 1
            while have == need:
                if not mn or len(s[l:r+1]) < len(mn):
                    mn = s[l:r+1]
                wndo[s[l]] = wndo.get(s[l], 0) - 1
                if s[l] in tgt and wndo[s[l]] < tgt[s[l]]:
                    have -= 1
                l += 1                
        return mn

if __name__ == '__main__':
    o = Solution()
    print(o.minWindow('ADOBECODEBANC', 'ABC'))
    print(o.minWindow('a', 'a'))
    print(o.minWindow('a', 'aa'))
