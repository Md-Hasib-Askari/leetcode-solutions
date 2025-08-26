from typing import List
from collections import deque


def solve(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n < 1:
        return []

    dq = deque([])
    res = []

    for i in range(k):
        el = nums[i]

        while dq and nums[dq[-1]] < el:
            dq.pop()

        if not dq or nums[dq[-1]] >= el:
            dq.append(i)

    res.append(nums[dq[0]])

    r = k
    while r < n:
        if dq and dq[0] < r - k + 1:
            dq.popleft()
        r_el = nums[r]
        
        while dq and nums[dq[-1]] < r_el:
            dq.pop()

        if not dq or nums[dq[-1]] >= r_el:
            dq.append(r)

        res.append(nums[dq[0]])
        r += 1

    return res

if __name__ == "__main__":
    print(solve([1, -1], 1))