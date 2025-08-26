def solve(s: str, t: str) -> str:
    n1 = len(s)
    n2 = len(t)
    if n1 < n2:
        return ""
    
    s_map = {}
    t_map = {}
    for ch in t:
        t_map[ch] = t_map.get(ch, 0) + 1
        s_map[ch] = 0

    have, need = 0, len(t_map)
    l, r = 0, 0
    min_len = float("inf")
    min_str = (-1, -1)

    while r < n1:
        char = s[r]
        if char in t_map:
            s_map[char] = s_map.get(char, 0) + 1
            if s_map[char] == t_map[char]:
                have += 1

        while have == need:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_str = (l, r)

            if s[l] in t_map:
                s_map[s[l]] -= 1
                if s_map[s[l]] < t_map.get(s[l], 0):
                    have -= 1
            l += 1

        r += 1

    return "" if min_str == (-1, -1) else s[min_str[0]: min_str[1] + 1]

if __name__ == "__main__":
    print(solve("ADOBECODEBANC", "ABC"))