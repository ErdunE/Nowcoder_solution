#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self , arr: List[int]) -> int:
        # write code here

        # 检查数组是否为空或小于1
        if len(arr) < 1:
            return 0

        # 设置结果变量，左右指针分别指向数组首尾，最大左右指针变量
        res = 0
        left = 0
        right = len(arr) - 1
        maxL = 0
        maxR = 0

        while left < right:
            # 判断当前左右指针最大值
            maxL = max(maxL, arr[left])
            maxR = max(maxR, arr[right])
            # 较小一方指针开始向前移动并计算存雨量
            if maxL < maxR:
                res = res + maxL - arr[left]
                left = left + 1
            else:
                res = res + maxR - arr[right]
                right = right - 1

        return res
            
            