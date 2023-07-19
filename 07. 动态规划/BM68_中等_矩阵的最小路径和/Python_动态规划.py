#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # write code here

        n = len(matrix) 
        m = len(matrix[0])

        # dp[i][j]表示以当前i，j位置为终点的最短路径长度
        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0][0] = matrix[0][0]

        # 处理第一列
        for i in range(1, n):
            dp[i][0] = matrix[i][0] + dp[i - 1][0]

        # 处理第一行
        for j in range(1, m):
            dp[0][j] = matrix[0][j] + dp[0][j - 1]

        # 按照公式来
        for i in range(1, n):
            for j in range(1, m):
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = matrix[i][j] + dp[i][j - 1]
                else:
                    dp[i][j] = matrix[i][j] + dp[i - 1][j]

        return dp[n - 1][m - 1]