# import pytest
import unittest
from median_sorted_arrays import Solution


class TestMedianSortedArrays(unittest.TestCase):
    def test_find_median_sorted_arrays(self):
        sol = Solution()

        assert sol.findMedianSortedArrays([1, 3], [2]) == 2
        assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
        assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0
        assert sol.findMedianSortedArrays([0], [0, 0]) == 0
        assert sol.findMedianSortedArrays([], [1]) == 1
        assert sol.findMedianSortedArrays([2], []) == 2
        assert sol.findMedianSortedArrays([1, 3], [2]) == 2


if __name__ == '__main__':
    unittest.main()

# @pytest.mark.parametrize('l1,l2,result', [([1, 3], [2], 2),
#                                           ([1, 2], [3, 4], 2.5),
#                                           ([0, 0], [0, 0], 0),
#                                           ([], [1], 1),
#                                           ([2], [], 2),
#                                           ([1, 3], [2], 2)])
# def test_find_median_sorted_arrays(l1, l2, result):
#     sol = Solution()
#     assert sol.findMedianSortedArrays(l1, l2) == result

# def test_find_median_sorted_arrays():
#     sol = Solution()
#     assert sol.findMedianSortedArrays([1, 3], [2]) == 2
#     assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
#     assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0
#     assert sol.findMedianSortedArrays([0], [0, 0]) == 0
#     assert sol.findMedianSortedArrays([], [1]) == 1
#     assert sol.findMedianSortedArrays([2], []) == 2
#     assert sol.findMedianSortedArrays([1, 3], [2]) == 2
