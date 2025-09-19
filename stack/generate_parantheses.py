def solve(n: int) -> list[str]:
    stack = []
    res = []

    def backtrack(openN: int, closeN: int):
        # base case: openN == closeN = n
        if openN == closeN == n:
            res.append("".join(stack))
            return
        
        # closeN < openN
        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN+1)
            stack.pop()

        # openN < n
        if openN < n:
            stack.append("(")
            backtrack(openN+1, closeN)
            stack.pop()

    backtrack(0, 0)

    return res

if __name__ == "__main__":
    n = 3
    print(solve(n))