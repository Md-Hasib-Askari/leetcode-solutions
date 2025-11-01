def solve(nums: list[int]) -> list[list[int]]:
    result = []
    
    subset = []
    def backtrack(start: int):
        if start == len(nums):
            result.append(subset.copy())
            return
        
        # Include nums[start]
        subset.append(nums[start])
        backtrack(start + 1)

        # Exclude nums[start]
        subset.pop()
        backtrack(start + 1)

    backtrack(0)
    return result

if __name__ == "__main__":
    tests = [ [1, 2, 3], [0], [1]]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
