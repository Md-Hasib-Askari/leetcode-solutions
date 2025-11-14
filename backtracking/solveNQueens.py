def solve(n: int) -> list[list[str]]:
    res = []
    board = [["."]*n for _ in range(n)]

    def is_overlapped(r, c):
        for i in range(n):
            for j in range(n):
                if board[i][j] == "Q" and (
                    abs(i - r) == abs(j - c) or
                    i == r or j == c
                ):
                    return True
        return False

    def backtrack(row, board):
        if row == n:
            res.append(["".join(r) for r in board])
            return

        for j in range(n):
            if is_overlapped(row, j):
                continue
            board[row][j] = "Q"
            backtrack(row + 1, board)
            board[row][j] = "."
    
    backtrack(0, board)

    return res

if __name__ == "__main__":
    tests = [4, 1]
    for test in tests:
        print(f"Input: {test}")
        # print(f"Output: {solve(test)}")
        output = solve(test)
        for board in output:
            for row in board:
                print(row)
            print()
            print()
        print("-" * 20)
