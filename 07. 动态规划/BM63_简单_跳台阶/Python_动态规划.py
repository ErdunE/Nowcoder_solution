#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here

        # 低于2项的数列，直接返回n
        if number <= 1:
            return 1

        # 创建一个长度为n+1的数组，因为只有n+1才能有下标第n项，我们用它记录前n项斐波那契数列
        temp = [0 for i in range(number + 1)]

        # 根据公式，初始化第0项和第1项。
        temp[0] = 1
        temp[1] = 1
        
        # 遍历数组，依照公式某一项等于前两项之和，将数组后续元素补齐，即可得到fib[n]。
        for i in range(2, number + 1):
            temp[i] = temp[i - 1] + temp[i - 2]

        return temp[number]