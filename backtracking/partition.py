def solve(s: str) -> list[list[str]]:
    res, path = [], []

    def is_palindrome(sub: str) -> bool:
        l = 0
        r = len(sub) - 1
        while l < r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True

    def backtrack(idx: int):
        if idx >= len(s):
            res.append(path[:])
            return
        
        for i in range(idx, len(s)):
            substr = s[idx:i+1]
            if is_palindrome(substr):
                path.append(substr)
                backtrack(i+1)
                path.pop()

    backtrack(0)
    return res

def solve2(s: str) -> list[list[str]]:
    res, part = [], []

    def is_palindrome(sub: str) -> bool:
        l = 0
        r = len(sub) - 1
        while l < r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        
        for j in range(i, len(s)):
            substr = s[i : j + 1]
            if is_palindrome(substr):
                part.append(substr)
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

if __name__ == "__main__":
    tests = [ 
        "aab",
        "a",
        "racecar",
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
