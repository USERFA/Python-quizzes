from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    numbers.insert(0,None)
    for i in range(1,len(numbers)):
        x = target - numbers[i]
        if x in numbers[i+1:] and x != numbers[i]:
            return [i,numbers[i+1:].index(x)+i+1]
        

print(twoSum([1,2,3,4],6))