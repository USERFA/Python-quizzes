from typing import List
def productExceptSelf(nums:List[int]) -> List[int]:
    output = []
    for i in range(len(nums)):
        product=1
        for j in range(len(nums)):
            if j != i:
                product *=nums[i]
        output.append(product)
    return output

print(productExceptSelf([1,2,3,4]))
#[24,12,8,6]