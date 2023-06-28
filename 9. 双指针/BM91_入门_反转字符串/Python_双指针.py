#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 反转字符串
# @param str string字符串 
# @return string字符串
#
class Solution:
    def solve(self , str: str) -> str:
        # write code here

        # 设置左右指针
        left = 0 
        right = len(str) - 1

        # 两指针同时往中间靠
        while left < right:
            res = list(str)
            temp = res[left]
            res[left] = res[right]
            # 交换左右指针的字符
            res[right] = temp
            str = ''.join(res)
            left = left + 1
            right = right - 1
        return str