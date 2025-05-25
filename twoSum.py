from typing import List

def twoSum(nums:List[int] , target:int) ->List[int]:
    for i in range(len(nums)):
        x = target - nums[i]
        for i,x in enumerate(nums):
            return [i, nums.index(x)]

print(twoSum([5,5],10))