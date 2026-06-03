class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        da = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for r in range(len(text1)):
            for c in range(len(text2)):
                da[r+1][c+1] = 1+da[r][c] if text1[r] == text2[c] else max(da[r+1][c], da[r][c+1])
        return da[-1][-1]
                
if __name__ == '__main__':
    o = Solution()
    print(o.longestCommonSubsequence('abcde', 'ace'))
    print(o.longestCommonSubsequence('abc', 'abc'))
    print(o.longestCommonSubsequence('abc', 'def'))