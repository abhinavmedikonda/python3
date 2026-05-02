class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        co, cn = image[sr][sc], color
        e = image
        vstd = set()
        def recur(r, c):
            if r in range(len(e)) and c in range(len(e[0])) and (r, c) not in vstd and e[r][c] == co:
                vstd.add((r, c))
                image[r][c] = cn
                recur(r-1, c)
                recur(r, c-1)
                recur(r+1, c)
                recur(r, c+1)
        recur(sr, sc)
        return e

if __name__ == '__main__':
    o = Solution()
    print(o.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    print(o.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
