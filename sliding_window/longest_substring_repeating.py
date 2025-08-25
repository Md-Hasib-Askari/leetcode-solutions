def max_freq(freq: dict) -> int:
    if not freq:
        return 0
    return max(freq.values())

def solve(s: str, k: int) -> int:
    n = len(s)
    l = 0
    freq = {}
    maxL = 0
    for r in range(n):
        freq[s[r]] = freq.get(s[r], 0) + 1
        while (r - l + 1) - max_freq(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        maxL = max(maxL, r - l + 1)
    return maxL

if __name__ == "__main__":
    s = "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
    k = 7
    print(solve(s, k))