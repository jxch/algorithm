# https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        a = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return 0 if a < -2**31 or a > 2**31 -1 else a