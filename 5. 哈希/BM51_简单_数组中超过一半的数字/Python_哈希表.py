#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here

        # 创建哈希表
        hash = dict()

        # 遍历数组
        for i in range(len(numbers)):
            # 如果数字在哈希表中
            if numbers[i] in hash:
                # 对应个数加1
                hash[numbers[i]] += 1
            else:
                # 反之没有的话 个数为1
                hash[numbers[i]] = 1
            
            # 一旦在哈希表中的个数超过数组的一半 返回该数字
            if hash[numbers[i]] > (int)(len(numbers)/2):
                return numbers[i]
        
        return 0