import sys
sys.stdin = open('../../input.txt', 'r')
 
def solve():
    n = int(input())
    
    count = 0
    for i in range(n // 2 + 1):
        for j in range(n // 4 + 1):
            if i * 2 + j * 4 == n:
                count += 1
    print(count)
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)