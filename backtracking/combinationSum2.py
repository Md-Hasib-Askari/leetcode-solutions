def solve(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates.sort()

    def backtrack(idx: int, path: list[int], curr_sum: int = 0):
        if curr_sum == target:
            res.append(path.copy())
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] + curr_sum > target: break

            path.append(candidates[i])
            backtrack(i+1, path, curr_sum+candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res

if __name__ == "__main__":
    tests = [ 
        ([10,1,2,7,6,1,5], 8),
        ([2,5,2,1,2], 5)
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
