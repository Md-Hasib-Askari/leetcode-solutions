def solve(prices):
    n = len(prices)
    if n < 2:
        return 0
    max_profit = 0
    min_price = prices[0]
    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit

if __name__ == "__main__":
    print(solve([7, 1, 5, 3, 6, 4]))
