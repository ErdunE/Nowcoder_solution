#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串 
# @param version2 string字符串 
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write code here

        # 计算两个版本的长度
        n1 = len(version1)
        n2 = len(version2)

        # 设置双指针
        i, j = 0, 0

        # 当任一指针超出版本长度后 停止
        while i < n1 or j < n2:
            # 创建临时变量用来存储整理后的版本1
            num1 = 0
            # 从下一个点前截取数字
            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1 
            # 跳过点           
            i += 1

            # 创建临时变量用来存储整理后的版本2
            num2 = 0
            # 从下一个点前截取数字
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1
            # 跳过点
            j += 1

            # 比较数字大小
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
                
        # 版本号相同        
        return 0