def knapsack(capacity, items):
    n = len(items)
    dp = [[0] * (n + 1) for _ in range(capacity + 1)]
    for r in range(1, capacity + 1):
        for c, (cw, cv) in enumerate(items, start=1):
            upon = cv+dp[r-cw][c] if r >= cw else 0 # c-1 for binary
            dp[r][c] = max(upon, dp[r][c-1])
    r, c = capacity, n
    counts = [0] * n
    while r > 0 and c > 0:
        # if value same as without this item, move left (to previous item)
        if dp[r][c] == dp[r][c-1]:
            c -= 1
        else:
            # we used at least one of item i-1; stay in same i and reduce w
            counts[c-1] += 1
            r -= items[c-1][0]
            # c -= 1 # for binary
    print(dp[capacity][n], counts)

if __name__ == '__main__':
    knapsack(6, ((2, 4), (4, 8)))
    knapsack(7, ((2, 3), (3, 4)))
    knapsack(100, ((1, 1),)) #[100]
    knapsack(100, ((100, 1),)) #[1]
    knapsack(100, ((1, 1),(3, 4))) #[1, 33]
    knapsack(100, ((60, 80), (50, 50))) #[0, 2]
    knapsack(100, ((10, 10), (30, 40), (56, 78))) #[1, 3, 0]
    knapsack(6, ((3, 4), (4, 5)))
