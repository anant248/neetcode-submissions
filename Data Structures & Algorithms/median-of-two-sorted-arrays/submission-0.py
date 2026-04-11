class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine the 2 arrays, sort return middle value
        newArr = nums1 + nums2
        newArr.sort()
        if len(newArr) % 2 == 1:
            mid = len(newArr) // 2
            return newArr[mid]
        else:
            mid1 = len(newArr) // 2
            mid2 = mid1 - 1
            return (newArr[mid1] + newArr[mid2]) / 2