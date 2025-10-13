def solve(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    l1, l2 = len(nums1), len(nums2)

    total = l1 + l2
    half = (total + 1) // 2

    l, r = 0, l1

    while l <= r:
        i = l + (r-l) // 2
        j = half - i

        Aleft = nums1[i-1] if i > 0 else float('-inf')
        Aright = nums1[i] if i < l1 else float('inf')
        Bleft = nums2[j-1] if j > 0 else float('-inf')
        Bright = nums2[j] if j < l2 else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return max(Aleft, Bleft)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

    return -1

if __name__ == "__main__":
    tests = [([1, 3], [2]), ([1, 2], [3, 4])]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
