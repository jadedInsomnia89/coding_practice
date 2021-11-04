import timeit
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        # start timer to determine runtime
        start = timeit.default_timer()

        # variables used for combined the list
        combined_lists_sorted = []
        nums1_mid, nums2_mid = 0, 0

        # print the two lists
        print(f'List 1: {nums1}')
        print(f'List 2: {nums2}')

        # merge the two sorted lists into nums1 new sorted list
        while nums1_mid < len(nums1) and nums2_mid < len(nums2):
            if nums1[nums1_mid] <= nums2[nums2_mid]:
                combined_lists_sorted.append(nums1[nums1_mid])
                nums1_mid += 1
            else:
                combined_lists_sorted.append(nums2[nums2_mid])
                nums2_mid += 1

        combined_lists_sorted = (combined_lists_sorted + nums1[nums1_mid:] +
                                 nums2[nums2_mid:])

        # print the combined list
        print(f'Combined lists: {combined_lists_sorted}')

        total = len(combined_lists_sorted)

        # calculate the median
        if total % 2 == 0:
            median_index1 = (total // 2) - 1
            median_index2 = total // 2
            mid_num1 = combined_lists_sorted[median_index1]
            mid_num2 = combined_lists_sorted[median_index2]
            median = (mid_num1 + mid_num2) / 2

        else:
            median_index = (total // 2)
            median = combined_lists_sorted[median_index]

        # print runtime before exiting the function
        stop = timeit.default_timer()
        print(f'Runtime: {(stop - start) * 1000:.3f} ms')

        return median


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int],
#                                nums2: List[int]) -> float:

#         # calculate the total of both lists and half of the total
#         total = len(nums1) + len(nums2)
#         half = total // 2
#         # ensure nums1 is the smaller list because we want to do a binary search on the smaller list
#         if len(nums2) < len(nums1):
#             nums1, nums2 = nums2, nums1

#         # left and right pointers for the first list
#         l, r = 0, len(nums1) - 1

#         while True:
#             # Calculate the index of the middle value for each list.
#             # Subtracting the mid of nums1 from half gives the number
#             # needed to make both partitions equal half (if they were combined).
#             # Two must be subtracted because we are calculating the index.
#             # Both lists start at 0 so 1 must be subtracted for each list.
#             nums1_mid = (l + r) // 2
#             nums2_mid = half - nums1_mid - 2

#             # calculate the max value for left partition and min value for right partition for both lists
#             nums1_left_part = nums1[nums1_mid] if nums1_mid >= 0 else float('-infinity')
#             nums1_right_part = nums1[nums1_mid + 1] if nums1_mid + 1 < len(nums1) else float('infinity')
#             nums2_left_part = nums2[nums2_mid] if nums2_mid >= 0 else float('-infinity')
#             nums2_right_part = nums2[nums2_mid + 1] if nums2_mid + 1 < len(nums2) else float('infinity')

#             # calculate the median because partitions are correct
#             if nums1_left_part <= nums2_right_part and nums2_left_part <= nums1_right_part:
#                 # odd number of elements
#                 if total % 2:
#                     return min(nums1_right_part, nums2_right_part)
#                 # even number of elements
#                 return (max(nums1_left_part, nums2_left_part) + min(nums1_right_part, nums2_right_part)) / 2

#             # the left partition has too many values so the r pointer is shifted one to the left of the mid value
#             elif nums1_left_part > nums2_right_part:
#                 r = nums1_mid - 1
#             # the left partition does not have enough values so the l pointer is shifted one to the right of the mid value
#             else:
#                 l = nums1_mid + 1
