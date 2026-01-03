def solve(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

if __name__ == "__main__":
    tests = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("", ""),
        ("a", "a"),
        ("a", "b"),
        ("abcdxyz", "xyzabcd"),
        ("AGGTAB", "GXTXAYB"),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
