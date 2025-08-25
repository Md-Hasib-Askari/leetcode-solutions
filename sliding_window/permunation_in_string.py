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

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidboaoo"
    print(solve(s1, s2))