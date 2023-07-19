#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # write code here

        # 优先检查特殊情况
        if len(s1) is None or len(s2) is None:
            return "-1"

        len1 = len(s1)
        len2 = len(s2)
        # #dp[i][j]表示第一个字符串到第i位，第二个字符串到第j位为止的最长公共子序列长度
        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
        # 遍历两个字符串每个位置求的最长长度
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # 遇到两个字符相等
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 遇到的两个字符不同
                else:
                    # 来自左边或者上方的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 从动态规划数组末尾开始
        i = len1
        j = len2
        s = []

        while dp[i][j] != 0:
            # 来自于左方向
            if dp[i][j] == dp[i - 1][j]:
                i = i - 1
            # 来自于上方向
            elif dp[i][j] == dp[i][j - 1]:
                j = j - 1
            # 来自于左上方向
            elif dp[i][j] > dp[i - 1][j - 1]:
                i = i - 1
                j = j - 1
                # 只有左上方向才是字符相等的情况，入栈，逆序使用
                s.append(s1[i])

        res = ""
        # #拼接子序列
        while len(s) != 0:
            res += s[-1]
            s.pop()
        # 如果两个完全不同，返回字符串为空，则要改成-1
        if res is None or res == "":
            return "-1"
        else:
            return res