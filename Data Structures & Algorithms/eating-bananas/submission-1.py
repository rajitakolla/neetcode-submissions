import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minimum, maximum = 1, max(piles)
        result = maximum

        while minimum <= maximum:

            mid = (minimum+maximum)//2

            time = 0

            for i in piles:
                time += math.ceil(float(i)/mid)

            if time <= h:
                result = mid
                maximum = mid-1
            else:
                minimum = mid+1

        return result

    