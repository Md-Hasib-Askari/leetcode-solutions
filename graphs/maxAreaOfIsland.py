def solve(grid: list[list[int]]) -> int:    
    m = len(grid)
    n = len(grid[0])
    max_area = 0

    area = 0
    def dfs(i, j):
        nonlocal max_area
        nonlocal area
        
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == 0:
            return
        
        print(i, j, area)
        grid[i][j] = 0
        area += 1
        max_area = max(max_area, area)

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = 0
                dfs(i, j)
    
    return max_area

if __name__ == "__main__":
    tests = [ 
        [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ],
        [[0,0,0,0,0,0,0,0]]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
