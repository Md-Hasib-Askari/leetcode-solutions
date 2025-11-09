def solve(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(visited: list[int]):
        if len(visited) == len(nums):
            res.append(visited.copy())
            return
              
        for i in range(len(nums)):
            if nums[i] in visited:
                continue

            # Include nums[i]
            visited.append(nums[i])
            backtrack(visited)
            visited.pop()

    backtrack([])
    return res

def solve_optimal(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(idx: int):
        if idx == len(nums):
            res.append(nums.copy())
            return

        for i in range(len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            backtrack(idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

    backtrack(0)
    return res

if __name__ == "__main__":
    tests = [ 
        [1, 2, 3],
        [0, 1],
        [1]
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
