class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        median_index = total // 2
        is_even = total % 2 == 0

        i = j = 0
        last = current = 0

        for _ in range(median_index + 1):
            last = current

            if i < n and (j >= m or nums1[i] <= nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

        if is_even:
            return (last + current) / 2
        else:
            return current
