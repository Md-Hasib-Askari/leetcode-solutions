class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = heights[0]
        stack = []
        n = len(heights)

        stack.append((0, heights[0]))

        for i in range(1, n):
            ndx = -1
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                area = (i-idx)*h
                max_area = max(max_area, area)
                ndx = idx
            stack.append((i if ndx == -1 else ndx, heights[i]))

        while stack:
            idx, h = stack.pop()
            area = (n-idx)*h
            max_area = max(max_area, area)

        return max_area
        

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10