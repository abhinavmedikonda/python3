from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        outp = 0
        deq = deque([(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 2] + [None])
        frsh = set([(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 1])
        while len(deq) > 1:
            item = deq.popleft()
            if not item:
                deq.append(None)
                outp += 1
                continue
            r, c = item
            if r > 0 and (r-1, c) in frsh:
                frsh.remove((r-1, c))
                deq.append((r-1, c))
            if c > 0 and (r, c-1) in frsh:
                frsh.remove((r, c-1))
                deq.append((r, c-1))
            if r < len(grid)-1 and (r+1, c) in frsh:
                frsh.remove((r+1, c))
                deq.append((r+1, c))
            if c < len(grid[0])-1 and (r, c+1) in frsh:
                frsh.remove((r, c+1))
                deq.append((r, c+1))
        return -1 if frsh else outp

if __name__ == '__main__':
    o = Solution()
    print(o.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(o.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(o.orangesRotting([[0,2]]))
