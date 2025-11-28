import sys

sys.stdin = open('../../input.txt', 'r')

input = sys.stdin.readline
output = sys.stdout.write

def solve():
    PRIMES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53
    ]
    n = int(input())
    a = list(map(int, input().split()))

    for p in PRIMES:
        for x in a:
            if x % p != 0:
                output(f"{p}\n")
                return
    
    output("-1\n")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)
