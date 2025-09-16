class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) // 2 == 1 and len(nums1) > 2:
            return nums1[len(nums1) // 2]
        else:
            a = nums1[len(nums1) // 2] + nums1[(len(nums1) - 1) // 2]
            return a / 2.0