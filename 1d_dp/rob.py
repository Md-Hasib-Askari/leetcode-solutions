def solve(nums: list[int]) -> int:
    dp = [-1]*len(nums)

    def dfs(i):
        if i >= len(nums):
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        rob_current = nums[i] + dfs(i + 2)
        skip_current = dfs(i + 1)
        dp[i] = max(rob_current, skip_current)
        
        return dp[i]

    return dfs(0)


if __name__ == "__main__":
    tests = [
        [2,7,9,3,1], # Expected output: 12
        [1,2,3,1], # Expected output: 4
        [1,2,3], # Expected output: 4
        [10,2,5,20,15,30], # Expected output: 55
        [5,5,10,100,10,5] # Expected output: 110
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
