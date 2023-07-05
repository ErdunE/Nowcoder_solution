#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here

        # 如果array为空即返回False
        if len(array) == 0:
            return False

        # 遍历每一行
        for i in range(len(array)):
            # 遍历每一列
            for j in range(len(array[0])):
                # 如果当前数字等于目标值则返回Ture
                if array[i][j] == target:
                    return True
                # 反之列+1 继续搜索
                else:
                    j += 1
                    continue
            # 所有列搜完后，行+1
            i += 1
        # 如果遍历整个二维数组后还没发现目标值，则返回False
        return False
                