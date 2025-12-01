def solve(nums: list[int]) -> int:
    currMin = currMax = 1
    res = nums[0]

    for n in nums:
        if n < 0:
            currMin, currMax = currMax, currMin
        
        currMax = max(n, currMax * n)
        currMin = min(n, currMin * n)

        res = max(res, currMax)
    return res

if __name__ == "__main__":
    tests = [
        [2,3,-2,4],
        [-2, 0, -1],
        [-2,3,-4],
        [0,2],
        [-1,-2,-3],
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
