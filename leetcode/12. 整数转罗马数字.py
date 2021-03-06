# https://leetcode-cn.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ""
        for i in range(len(integer)):
            while num >= integer[i]:
                res += roman[i]
                num -= integer[i]
        return res