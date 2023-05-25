"""Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))."""


class Solution(object):

    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_length = m + n
        half_length = (total_length + 1) // 2

        left, right = 0, m

        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = half_length - partition_nums1

            max_left_nums1 = float("-inf") if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float("inf") if partition_nums1 == m else nums1[partition_nums1]
            max_left_nums2 = float("-inf") if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float("inf") if partition_nums2 == n else nums2[partition_nums2]

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if total_length % 2 == 0:
                    median = (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2.0
                else:
                    median = max(max_left_nums1, max_left_nums2)
                return median
            elif max_left_nums1 > min_right_nums2:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1

        raise ValueError("Input arrays are not sorted!")


if __name__ == '__main__':
    solution = Solution()
    print(solution.find_median_sorted_arrays([1, 2], [3, 4]))
