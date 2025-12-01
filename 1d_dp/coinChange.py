def solve(coins: list[int], amount: int) -> int:
    dp = {}

    def dfs(amnt) -> int:
        if amnt == 0:
            return 0
        if amnt in dp:
            return dp[amnt]
        
        res = float('inf')
        for coin in coins:
            if amnt - coin >= 0:
                res = min(res, 1 + dfs(amnt-coin))
                # print(f"amnt: {amnt}, coin: {coin}, dp: {dp}")
        
        dp[amnt] = res
        return dp[amnt]
    minCoins = dfs(amount)
    return -1 if minCoins >= float('inf') else minCoins

if __name__ == "__main__":
    tests = [
        ([1,2,5], 11),
        ([2], 3),
        ([1], 0),
        ([186,419,83,408], 6249),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
