from typing import List


def search(nums: List[int], target: int) -> int:
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # else:
    #     return -1
    middle = 0
    left = 0
    right = len(nums)
    for i in range(len(nums)):
        middle = (len(nums) - 1) // 2
        if nums[middle] == target:
            return middle
        else:
            while(left<right):
                if nums[left] ==target:
                    return left
                left+=1
            else:
                return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
