#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here

        # 低于2项的数列，直接返回n
        if n < 2:
            return n
        
        # 初始化第0项，与第1项分别为0，1
        res = 0
        a = 0
        b = 1

        # 从第2项开始，逐渐按照公式累加，并更新相加数始终为下一项的前两项
        for i in range(2, n + 1):
            res = (a + b)
            a = b
            b = res

        return res