class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # optimal, running binary search on the smaller of the two arrays
        # time: O(log(min(m,n)))
        # space: O(1)
        # we will do binary search on A so make sure A is the smaller one
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        # binary search pointer for A
        l, r = 0, len(A) - 1
        while True:
            midA = l + (r - l) // 2 # mid point for A
            midB = half - midA - 2 # accordingly mid point for B

            Aleft = A[midA] if midA >= 0 else float("-inf")
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("inf")
            Bleft = B[midB] if midB >= 0 else float("-inf")
            Bright = B[midB + 1] if (midB + 1) < len(B) else float("inf")

            # check if Aleft <= Bright and vice-versa, this means left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1: # odd length
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # partition for A is too big
                r = midA - 1
            else:                # partition for A is too small
                l = midA + 1
