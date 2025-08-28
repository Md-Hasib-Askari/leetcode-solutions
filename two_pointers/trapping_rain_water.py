def solve():
    height = [4,2,0,3,2,5]

    n = len(height)
    left_max = [1e9] * n
    right_max = [1e9] * n
    water_trapped = 0

    # Compute left max heights
    ptr_a = 0
    ptr_b = 0

    while ptr_b < n:
        if height[ptr_b] >= height[ptr_a]:
            left_max[ptr_b] = 0
            ptr_a = ptr_b
        else:
            left_max[ptr_b] = min(left_max[ptr_b], height[ptr_a]-height[ptr_b])
        ptr_b += 1

    # Compute right max heights
    ptr_a = n - 1
    ptr_b = n - 1

    while ptr_b >= 0:
        if height[ptr_b] >= height[ptr_a]:
            right_max[ptr_b] = 0
            ptr_a = ptr_b
        else:
            right_max[ptr_b] = min(right_max[ptr_b], height[ptr_a]-height[ptr_b])
        ptr_b -= 1

    print(left_max)
    print(right_max)

    # Calculate water trapped
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) 

    print(water_trapped)

def main():
    # t = int(input())
    t = 1  # For testing purposes, set to 1
    for _ in range(t):
        solve()  # implement per problem

if __name__ == "__main__":
    main()