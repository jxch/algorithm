# https://leetcode-cn.com/problems/regular-expression-matching/

# 位图
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for j in range(2,n+1):
            dp[0][j]=dp[0][j-2] and p[j-1]=='*'
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j]=p[j-2] in {s[i-1],'.'} and dp[i-1][j] or dp[i][j-2]
                else:
                    dp[i][j]=p[j-1] in {s[i-1],'.'} and dp[i-1][j-1]
        return dp[m][n]