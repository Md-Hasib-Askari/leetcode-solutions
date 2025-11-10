def solve(board: list[list[str]], word: str) -> bool:
    res = set()

    m = len(board)
    n = len(board[0])
    def backtrack(i, j, idx):
        if idx == len(word):
            return True
        
        if (i >= m or j >= n or 
            i < 0 or j < 0 or 
            word[idx] != board[i][j] or 
            (i, j) in res): 
            return False

        res.add((i, j))
        found = (backtrack(i + 1, j, idx+1) or
                 backtrack(i - 1, j, idx+1) or
                 backtrack(i, j + 1, idx+1) or
                 backtrack(i, j - 1, idx+1))
        res.remove((i, j))
        return found

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    return False

if __name__ == "__main__":
    tests = [ 
        # ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        # ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
