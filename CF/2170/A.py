# A. Maximum Neighborhood

import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write
 
def solve():
    n = int(input())
 
    arr = []
    for i in range(1, n + 1):
        subarr = []
        for j in range(1, n + 1):
            num = (i-1) * n + j
            subarr.append(num)
        arr.append(subarr)
    
    max_sum = 0
    for i in range(n):
        for j in range(n):
            sm = arr[i][j]
            if i-1 >= 0:
                sm += arr[i-1][j]
            if i+1 < n:
                sm += arr[i+1][j]
            if j-1 >= 0:
                sm += arr[i][j-1]
            if j+1 < n:
                sm += arr[i][j+1]
            max_sum = max(max_sum, sm)
    output(f"{max_sum}\n")
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)