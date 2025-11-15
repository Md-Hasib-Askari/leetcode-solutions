def solve(n: int) -> int:
    if n <= 2:
        return n
    
    prev, curr = 1, 2
    for i in range(3, n+1):
        sum = prev + curr
        prev = curr
        curr = sum

    return curr

def solve_dp(n: int) -> int:
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

if __name__ == "__main__":
    tests = [2,3,4,5]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
