from collections import deque

def solve(grid: list[list[int]]) -> int:
    q = deque()
    rows, cols = len(grid), len(grid[0])
    fresh_count = 0
    time = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while q and fresh_count > 0:
        length = len(q)
        for _ in range(length):
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc))
        
        time += 1

    return time if fresh_count == 0 else -1

if __name__ == "__main__":
    tests = [
        [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ],
        [[2,1,1],[0,1,1],[1,0,1]],
        [[0,2]]
    ]

    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
