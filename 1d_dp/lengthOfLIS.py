def solve(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    tests = [ 
        [10,9,2,5,3,7,101,18],
        [0,1,0,3,2,3],
        [7,7,7,7,7,7,7],
        [4,10,4,3,8,9]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
