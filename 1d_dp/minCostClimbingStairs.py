def solve(cost: list[int]) -> int:
    dp = [0]*len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    return min(dp[-1], dp[-2])

if __name__ == "__main__":
    tests = [
        [10, 15, 20],
        [1,100,1,1,1,100,1,1,100,1]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)


# [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#  0  1    2  3  4   5   6  7   8   9
#  1  100  2  3  3  103  4  5  104  6    

