from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    data = zip(*matrix)
    print(data)
    exists = False
    for i in data:
        print(i)
        if target in i:
            return True
    else:
        return False
            



print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], -1))