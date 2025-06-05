from typing import List


def findMin(nums: List[int]) -> int:
    nums = sorted(nums)
    print(nums)
    return nums[0]