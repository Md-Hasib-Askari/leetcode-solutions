def solve(nums: list[int]) -> bool:
    sum_n = sum(nums)
    if sum_n % 2 == 1:
        return False
    target = sum_n // 2
    n = len(nums)

    dp = set()
    dp.add(0)
    for num in nums:
        next_dp = dp.copy()
        for t in dp:
            if t + num == target:
                return True
            if t + num < target:
                next_dp.add(t + num)
        dp = next_dp

    return False


if __name__ == "__main__":
    tests = [
        [1, 5, 11, 5],
        [1, 2, 3, 5]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
