# https://leetcode-cn.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s

        res = [''] * numRows
        n = 2 * numRows - 2

        for i, c in enumerate(s):
            res[min(idx := i % n, n - idx)] += c
        
        return ''.join(res)