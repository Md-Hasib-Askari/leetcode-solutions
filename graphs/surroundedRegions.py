def solve(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])

    def dfs(r, c):
        if board[r][c] != "O":
            return
        
        board[r][c] = "T"
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                dfs(nr, nc)

    for i in range(m):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][n-1] == "O":
            dfs(i, n-1)

    for i in range(n):
        if board[0][i] == "O":
            dfs(0, i)
        if board[m-1][i] == "O":
            dfs(m-1, i)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"

if __name__ == "__main__":
    tests = [
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X"]]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
