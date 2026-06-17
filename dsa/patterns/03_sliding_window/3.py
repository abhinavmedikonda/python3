from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(lambda: -1)
        l = 0
        maxi = 0
        for r in range(len(s)):
            if hmap[s[r]] >= l:
                l = 1+hmap[s[r]]
            else:
                maxi = max(maxi, r-l+1)
            hmap[s[r]] = r
        return maxi

if __name__ == '__main__':
    o = Solution()
    print(o.lengthOfLongestSubstring('abcabcbb'))
    print(o.lengthOfLongestSubstring('bbbbb'))
    print(o.lengthOfLongestSubstring('pwwkew'))
