def solve(s: str) -> str:
    resIdx, resLen = 0, 0
    n = len(s)

    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r-l+1 > resLen:
                resIdx = l
                resLen = r-l+1
            l -= 1
            r += 1
        
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            if r-l+1 > resLen:
                resIdx = l
                resLen = r-l+1
            l -= 1
            r += 1

    return s[resIdx: resIdx + resLen]

if __name__ == "__main__":
    tests = [
        "babad",
        "cbbd"
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
