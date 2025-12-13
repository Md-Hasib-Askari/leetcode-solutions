def solve(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    prereq = {c: [] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    return output


if __name__ == "__main__":
    tests = [
        (2, [[1,0]]),
        (4, [[1,0],[2,0],[3,1],[3,2]])
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
