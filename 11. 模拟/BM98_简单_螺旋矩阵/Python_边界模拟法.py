#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix: List[List[int]]) -> List[int]:
        # write code here

        # 创建结果数组
        res = list()
        n = len(matrix)

        # 排除特殊情况
        if n == 0:
            return res

        # 左右上下四个边界
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = n - 1

        # 循环直至边界重合
        while left <= right and up <= down:

            # 上边界的从左到右
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            # 上边界往下1
            up += 1
            if up > down:
                break

            # 右边界的从上到下
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            # 右边界往左1
            right -= 1
            if left > right:
                break

            # 下边界的从右往左
            i = right
            while i >= left:
                res.append(matrix[down][i])
                i -= 1
            # 下边界往上1
            down -= 1
            if up > down:
                break

            # 左边界的从下往上
            i = down
            while i >= up:
                res.append(matrix[i][left])
                i -= 1
            # 左边界往右1
            left += 1
            if left > right:
                break
        
        return res