# https://leetcode-cn.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for j in range(len(s), -1, -1):
            for i in range(len(s)-j, -1, -1):
                if (s[i:i+j]) == s[i:i+j][::-1]:
                    return s[i:i+j][::-1]