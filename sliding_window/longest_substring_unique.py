def solve():
    n = len(s)
    if n < 1:
        return 0
    if n == 1:
        return 1
    l = 0
    r = 1
    dup = set(s[l])
    maxL = 0
    while r < n and l < r:
        if s[r] in dup:
            l += 1
            dup.remove(s[l-1])
        else:
            dup.add(s[r])
            r += 1
        maxL = max(maxL, r-l+1)
    
    return maxL

if __name__ == "__main__":
    s = "abcabcbb"
    print(solve())