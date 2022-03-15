# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        substring = ''
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
            else:
                repeat_index = substring.find(s[i])
                substring = substring[repeat_index+1:] + s[i]
            res = max(res, len(substring))
        return res
