def solve(target: int, position: list[int], speed: list[int]) -> int:
    stack = []
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)

    for p,s in pairs:
        t = (target - p)/s
        stack.append(t)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop() 
    return len(stack)

if __name__ == "__main__":
    print(solve(100, [0,2,4], [4,2,1]))