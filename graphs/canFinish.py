def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # Map each course to its prerequisites
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # Store all courses along the current DFS path
    visiting = set()

    def dfs(crs):
        if crs in visiting:
            # Cycle detected
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
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
