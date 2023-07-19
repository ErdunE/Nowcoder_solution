#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param m int整型 
# @param n int整型 
# @return int整型
#
class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        # write code here

        # dp[i][j]表示大小为i*j的矩阵的路径数量
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 只有1行的时候，只有一种路径
                if i == 1:
                    dp[i][j] = 1
                    continue
                # 只有1列的时候，只有一种路径
                if j == 1:
                    dp[i][j] = 1
                    continue
                # 路径数等于左方格子的路径数加上上方格子的路径数
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]