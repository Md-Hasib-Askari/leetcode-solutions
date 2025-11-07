def solve(nums: list[int]) -> list[list[int]]:
    result = []

    nums.sort()
    
    subset = []
    def backtrack(start: int):
        if start == len(nums):
            subset_copy = subset[:]
            if subset_copy not in result:
                result.append(subset_copy)
                
            return
        
        # Include nums[start]
        subset.append(nums[start])
        backtrack(start + 1)

        # Exclude nums[start]
        subset.pop()
        backtrack(start + 1)

    backtrack(0)
    return result

def solve_2(nums: list[int]) -> list[list[int]]:
    result = []

    nums.sort()
    
    subset = []
    def backtrack(start: int):
        result.append(subset[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

    backtrack(0)
    return result

if __name__ == "__main__":
    tests = [
        [4,4,4,1,4],
        [1, 2, 2],
        [0],
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print(f"length: {len(solve(test))}")
        print("-" * 20)
