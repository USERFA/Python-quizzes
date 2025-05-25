from typing import List
def hasDuplicate(nums:List[int])->bool:
    hasDuplicate=False

    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]==nums[j]:
    #             hasDuplicate=True
    #             break

    # return hasDuplicate
    sets=set(nums)
    if(len(nums)==len(sets)):
        return False
    else:
        return True

print(hasDuplicate([1,2,3,4]))