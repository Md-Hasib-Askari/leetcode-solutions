import math 

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        avg = math.ceil(sum(piles) / h)
        mx = max(piles)
        res = mx

        low, high = avg, mx

        while low <= high:
            k = low + (high - low) // 2
            summ = 0
            for p in piles:
                summ += math.ceil(p / k)
            
            if summ <= h:
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1

        return res

if __name__ == '__main__':
    test = [
        ([3,6,7,11], 8),
        ([30,11,23,4,20], 5),
        ([30,11,23,4,20], 6)
    ]

    s = Solution()
    for t in test:
        res = s.minEatingSpeed(t[0], t[1])
        print(res)