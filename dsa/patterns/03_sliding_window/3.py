from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        bkt = {s[0]}
        l, r = 0, 1
        mx = 1
        while l < r and r < len(s):
            if s[r] in bkt:
                while s[l] != s[r]:
                    bkt.remove(s[l])
                    l += 1
                l += 1
            else:
                bkt.add(s[r])
            mx = max(mx, r-l+1)
            r += 1
        return mx

if __name__ == '__main__':
    o = Solution()
    print(o.lengthOfLongestSubstring('abcabcbb'))
    print(o.lengthOfLongestSubstring('bbbbb'))
    print(o.lengthOfLongestSubstring('pwwkew'))
