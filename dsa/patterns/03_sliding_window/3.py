import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        outp = -sys.maxsize
        l, r = 0, 0
        while r < len(s):
            if s[r] in hmap:
                for v in s[l:hmap[s[r]]]:
                    hmap.pop(v)
                l = 1+hmap[s[r]]
            outp = max(outp, r-l+1)
            hmap[s[r]] = r
            r += 1
        return outp if s else 0

if __name__ == '__main__':
    o = Solution()
    print(o.lengthOfLongestSubstring('abcabcbb'))
    print(o.lengthOfLongestSubstring('bbbbb'))
    print(o.lengthOfLongestSubstring('pwwkew'))
