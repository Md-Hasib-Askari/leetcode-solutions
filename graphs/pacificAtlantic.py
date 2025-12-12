def solve(heights: list[list[int]]) -> list[list[int]]:
    m, n = len(heights), len(heights[0])

    pacific = [[False]*n for _ in range(m)]
    atlantic = [[False]*n for _ in range(m)]

    def dfs(r, c, visited):
        visited[r][c] = True
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                if not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

    for i in range(m):
        dfs(i, 0, pacific)
    for i in range(n):
        dfs(0, i, pacific)

    for i in range(m):
        dfs(i, n-1, atlantic)
    for i in range(n):
        dfs(m-1, i, atlantic)

    res = []
    for r in range(m):
        for c in range(n):
            if pacific[r][c] and atlantic[r][c]:
                res.append([r,c])

    print("Pacific Reachable:")
    for row in pacific:
        print(row)
    print("Atlantic Reachable:")
    for row in atlantic:
        print(row)
    return res

if __name__ == "__main__":
    tests = [
        [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
        [[1]]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
