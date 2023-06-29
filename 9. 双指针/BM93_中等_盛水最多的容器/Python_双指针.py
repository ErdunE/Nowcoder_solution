#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param height int整型一维数组 
# @return int整型
#
class Solution:
    def maxArea(self , height: List[int]) -> int:
        # write code here

        # 特殊情况处理
        if len(height) < 2:
            return 0

        # 设置结果变量，左右指针分别指向数组首尾
        res = 0
        left = 0 
        right = len(height) - 1

        while left < right:
            # 计算左右指针范围内的面积大小以较短指针为高，并记录面积大小
            capacity = min(height[left], height[right]) * (right - left)
            # 依次比较面积大小并保留较大的
            res = max(res, capacity)
            # 较短指针向前移动
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return res