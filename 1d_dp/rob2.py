def solve(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    
    if n == 1:
        return nums[0]

    memo1 = [-1]*n
    memo2 = [-1]*n

    def dfs(i, ln, memo):
        if i >= ln:
            return 0
        
        if memo[i] != -1:
            return memo[i]
        
        memo[i] = max(nums[i] + dfs(i+2, ln, memo), dfs(i+1, ln, memo))
        return memo[i]
    
    return max(dfs(0, n-1, memo1), dfs(1, n, memo2))

if __name__ == "__main__":
    tests = [ 
        [2,7,9,3,1], # Expected output: 11
        [1,2,3,1], # Expected output: 4
        [1,2,3], # Expected output: 3
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
