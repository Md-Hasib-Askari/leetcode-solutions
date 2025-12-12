def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[0]*numCourses for _ in range(numCourses)]
    visited = [False]*numCourses

    for a, b in prerequisites:
        graph[b][a] = 1

    def dfs(start, visited):
        if visited[start]:
            return False
        
        visited[start] = True

        for neighbor in range(numCourses):
            if graph[start][neighbor] == 1:
                if visited[neighbor]:
                    return False
                if not dfs(neighbor, visited):
                    return False
                
        visited[start] = False
        return True
    
    for course in range(numCourses):
        if not dfs(course, visited):
            return False
    
    return True

if __name__ == "__main__":
    tests = [
        (2, [[1,0]]),
        (2, [[1,0],[0,1]])
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
