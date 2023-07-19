#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here

        # 设置结果字符串
        res = ""
        # 设置左指针
        left = 0

        # 如果str1中的字符在str2，左指针往右移动直到没有
        for i in range(len(str1) + 1):
            if str1[left:i+1] in str2:
                res = str1[left:i+1]
            else:
                left += 1

        return res