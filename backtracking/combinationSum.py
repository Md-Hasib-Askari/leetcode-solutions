def solve(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    candidates.sort()

    track = []
    def dfs():
        nonlocal track
        if sum(track) > target:
            return

        if sum(track) == target:
            sorted_track = sorted(track)
            if sorted_track not in res:
                res.append(sorted_track.copy())
                return
        
        for i in range(len(candidates)):
            if sum(track) + candidates[i] > target:
                continue
            track.append(candidates[i])
            dfs()
            track.pop()

    dfs()

    return res

if __name__ == "__main__":
    tests = [ 
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
