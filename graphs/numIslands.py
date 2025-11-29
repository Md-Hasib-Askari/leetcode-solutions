def solve(grid: list[list[str]]) -> int:
    m = len(grid)
    n = len(grid[0])

    res = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] == "0":
            return
        
        grid[i][j] = "0"

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)


    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)

    return res
    

if __name__ == "__main__":
    tests = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
