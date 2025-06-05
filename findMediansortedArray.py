def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
            totalNums=sorted(nums1+nums2)
            left = 0
            right = len(totalNums)-1
            mid=(left+right)//2

            if(len(totalNums)%2==0):
                median = (totalNums[mid]+totalNums[mid+1])/2
            else:
                median = totalNums[mid]
            return median