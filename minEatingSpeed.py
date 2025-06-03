import math
from typing import List


def minEatingSpeed( piles: List[int], h: int) -> int:
    lower = 1
    upper = max(piles)
    while lower < upper:
        mid = (lower+upper)//2
        summ = 0

        for i in range(len(piles)):
            summ += math.ceil(piles[i]/mid)
        
        # hours = sum(math.ceil(p / mid) for p in piles)
        # print('hours',hours ,'summ', summ)
        if summ <= h:
                upper = mid
        else:
                lower = mid+1  
    return lower

print(minEatingSpeed([1,4,3,2],9))
print(minEatingSpeed([25,10,23,4],4))
print(minEatingSpeed([3,6,7,11],8))