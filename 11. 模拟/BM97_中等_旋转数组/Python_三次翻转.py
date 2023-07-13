#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self , n: int, m: int, a: List[int]) -> List[int]:
        # write code here

        # 取余，因为每次长度为n的旋转数组相当于没有变化
        m = m % n
        # 第一次逆转全部数组元素
        a.reverse()
        # 第二次只逆转开头m个
        b = a[:m]
        b.reverse()

        # 第三次只逆转结尾m个
        c = a[m:]
        c.reverse()

        a[:m] = b
        a[m:] = c

        return a