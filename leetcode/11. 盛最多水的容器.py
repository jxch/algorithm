# https://leetcode-cn.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, left, right = 0, 0, len(height) - 1        
        while left < right:
            ans = max(ans, (right-left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        
        return ans
