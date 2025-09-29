class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        res = nums[0]

        while left < right:
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        res = min(res, nums[left])
        
        return res

if __name__ == '__main__':
    tests = [
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17]
    ]
    s = Solution()
    for t in tests:
        res = s.findMin(t)
        print(res)