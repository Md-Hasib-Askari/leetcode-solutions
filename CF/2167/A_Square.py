import sys
sys.stdin = open('../../input.txt', 'r')

def solve():
    nums = list(map(int, input().split()))

    all_equal = lambda lst: all(x == lst[0] for x in lst)

    if all_equal(nums):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)
