from collections import deque

def solve(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {i: [] for i in range(numCourses)}
    in_out = [0]*numCourses
    for a,b in prerequisites:
        graph[a].append(b)
        in_out[b] += 1
    
    q = deque()
    for i in range(numCourses):
        if in_out[i] == 0:
            q.append(i)
    
    finish = 0
    res = []
    while q:
        nd = q.popleft()
        res.append(nd)
        finish += 1

        for neighbor in graph[nd]:
            in_out[neighbor] -= 1
            if in_out[neighbor] == 0:
                q.append(neighbor)

    if finish != numCourses:
        return []
    return res[::-1]


if __name__ == "__main__":
    tests = [
        (2, [[1,0]]),
        (4, [[1,0],[2,0],[3,1],[3,2]])
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
