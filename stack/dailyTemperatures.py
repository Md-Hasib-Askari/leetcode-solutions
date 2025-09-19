def solve(T: list[int]) -> list[int]:
    n = len(T)
    ans = [0] * n
    for i in range(n-2, -1, -1):
        j = i + 1
        while j < n and T[j] <= T[i]:
            if ans[j] == 0:
                j = n      # give up: no warmer day ahead
            else:
                j += ans[j]  # jump forward using DP
        if j < n:
            ans[i] = j - i
    return ans

if __name__ == "__main__":
    temps = [73,74,75,71,69,72,76,73]
    print(solve(temps))  # [1,1,4,2,1,1,0,0]