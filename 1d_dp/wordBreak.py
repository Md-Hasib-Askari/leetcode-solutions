def solve(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    dp = [False]*(n+1)
    dp[n] = True

    for i in range(n, -1, -1):
        for j in range(i+1, n+1):
            if s[i:j] in wordDict and dp[j]:
                dp[i] = True
                break
    return dp[0]

if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple","pen"]),
        ("catsandog", ["cats","dog","sand","and","cat"]),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)