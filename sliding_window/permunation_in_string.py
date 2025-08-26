def compare_str(c1: dict, s2: str) -> bool:
    """
        Compare the character counts of two strings not considering their order.
    """
    c2 = {}
    for c in s2:
        c2[c] = c2.get(c, 0) + 1
    return c1 == c2

def solve(s1: str, s2: str) -> bool:
    """
        Check if any permutation of s1 is a substring of s2.
        Window size will always be fixed for this problem.
    """

    res = False
    n1 = len(s1)
    n2 = len(s2)
    l = 0
    r = l + n1

    c1 = {}
    for c in s1:
        c1[c] = c1.get(c, 0) + 1

    while r <= n2:
        if compare_str(c1, s2[l:r]):
            res = True
            break
        l += 1
        r += 1
    return res

def solve_optimal(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    matches = 0

    c1, c2 = [0] * 26 , [0] * 26

    for i in range(n1):
        c1[ord(s1[i]) - ord('a')] += 1
        c2[ord(s2[i]) - ord('a')] += 1

    for i in range(26):
        if c1[i] == c2[i]:
            matches += 1

    l = 0
    for r in range(n1, n2):
        # add new character
        idx = ord(s2[r]) - ord('a')
        c2[idx] += 1
        if c1[idx] == c2[idx]:
            matches += 1
        elif c1[idx] == c2[idx] - 1:
            matches -= 1

        # remove leftmost character
        idx = ord(s2[l]) - ord('a')
        c2[idx] -= 1
        if c1[idx] == c2[idx]:
            matches += 1
        elif c1[idx] == c2[idx] + 1:
            matches -= 1
        l += 1

    return matches == 26

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(solve_optimal(s1, s2))