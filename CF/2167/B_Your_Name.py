import sys
sys.stdin = open('../../input.txt', 'r')

def solve():
    n = int(input())
    s, t = input().split(" ")

    if sorted(s) == sorted(t):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)
