# https://leetcode-cn.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smin, smax = min(strs), max(strs)
        for i , item in enumerate(smin):
            if item != smax[i]:
                return smax[:i]
        return smin

