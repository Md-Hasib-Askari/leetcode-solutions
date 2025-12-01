def solve(s: str) -> int:
    n = len(s)
    dp = {n: 1}

    def dfs(i: int) -> int:
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0

        res = dfs(i + 1)
        if i + 1 < n and int(s[i : i + 2]) <= 26:
            res += dfs(i + 2)

        dp[i] = res
        return res
    return dfs(0)

def solve_bottom_up(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < n and int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
    return dp[0]

if __name__ == "__main__":
    tests = [
        "12",
        "226",
        "06"
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
