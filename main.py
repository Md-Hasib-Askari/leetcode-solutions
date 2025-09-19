
def solve(arr: list[int]) -> None:
    res = 0

    l = 0
    r = 1

    # pairs
    while r < len(arr):
        if l % 2 == 1:
            if arr[l] < arr[r]:
                dec = arr[r] - arr[l]
                arr[r] -= dec
                res += dec
        else:
            if arr[r] < arr[l]:
                dec = arr[l] - arr[r]
                arr[l] -= dec
                res += dec

        l += 1
        r += 1
    
    l = 0
    r = 1
    while l+2 < len(arr):
        if arr[r] < arr[l] + arr[l+2]:
            diff = arr[l] + arr[l+2] - arr[r]
            reduce = min(diff, arr[l+2])
            arr[l+2] -= reduce
            diff -= reduce
            res += reduce
            if diff > 0:
                reduce = min(diff, arr[l])
                arr[l] -= reduce
                diff -= reduce
                res += reduce

        l += 2
        r += 2

    print(res)

    

if __name__ == "__main__":
    import sys

    # If testing locally from a file, uncomment the next line:
    # sys.stdin = open("input.txt", "r")

    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)

    t = next(it)                       # number of test cases

    for _ in range(t):
        n = next(it)                   # size of the array for this test
        arr = [next(it) for _ in range(n)]
        solve(arr)
