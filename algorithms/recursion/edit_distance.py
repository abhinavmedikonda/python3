'''
72. Edit Distance
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recur(o, n):
            if (o, n) in hmap:
                return hmap[(o, n)]
            if o == len(word1):
                return len(word2)-n
            if n == len(word2):
                return len(word1)-o
            if word1[o] == word2[n]:
                outp = recur(o+1, n+1)
            else:
                outp = 1 + min(
                    recur(o, n+1), #insert
                    recur(o+1, n), #delete
                    recur(o+1, n+1) # update
                )
            hmap[(o, n)] = outp
            return outp
        hmap = {}
        return recur(0, 0)

if __name__ == '__main__':
    o = Solution()
    print(o.minDistance('horse', 'ros'))
    print(o.minDistance('intention', 'execution'))
