# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return ((nums[int(len(nums) / 2 - 1)] + nums[int(len(nums) / 2)]) / 2)
        else:
            return nums[len(nums) // 2]
