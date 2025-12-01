import sys
sys.stdin = open('../../input.txt', 'r')
 
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    even_count = sum(1 for x in nums if x % 2 == 0)
    odd_count = n - even_count
 
    res = None
    if even_count >= 1 and odd_count >= 1:
        res = sorted(nums)
    else:
        res = nums
 
    print(" ".join(map(str, res)))
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)