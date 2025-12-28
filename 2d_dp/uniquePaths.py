def solve(m: int, n: int) -> int:
    row = [1] * n

    for _ in range(m-1):
        newRow = [1]*n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    
    return row[0]

if __name__ == "__main__":
    tests = [
        (3, 7),
        (3, 2),
        (7, 3),
        (3, 3)
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)