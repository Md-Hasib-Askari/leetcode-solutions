import sys
sys.stdin = open('../../input.txt', 'r')

def solve():
    nums = list(map(int, input().split()))

    sorted_nums = sorted(nums)

    if sorted_nums[2] - sorted_nums[0] >= 10:
        print("check again")
    else:
        print(f"final {sorted_nums[1]}")

if __name__ == "__main__":
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)
