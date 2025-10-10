def solve(nums: list[int]) -> int:
    for _ in range(len(nums)):
        if nums[0] == nums[nums[0]]:
            return nums[0]
        
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]


if __name__ == "__main__":
    tests = [ 
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [3, 3, 3, 3, 3]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
