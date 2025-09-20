def solveDP(T: list[int]) -> list[int]:
    n = len(T)
    res = [0]*n

    for i in range(n-2, -1, -1):
        j = i + 1
        while j < n and T[j] <= T[i]:
            if res[j] == 0:
                j = n
            else:
                j += res[j]
        
        if j < n:
            res[i] = j - i    
    return res

def solve(temperatures: list[int]) -> list[int]:
    stack = []
    res = [0]*len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, idx = stack.pop()
            res[idx] = i - idx
        stack.append((t, i))
    return res

if __name__ == "__main__":
    temps = [73,74,75,71,69,72,76,73]
    print(solve(temps))  # [1,1,4,2,1,1,0,0]
    print(solveDP(temps))  # [1,1,4,2,1,1,0,0]