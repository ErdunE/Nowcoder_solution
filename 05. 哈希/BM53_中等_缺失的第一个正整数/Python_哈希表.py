#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here

        # 创建哈希表
        hash = dict()

        # 哈希表记录数组中出现的每个数字
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1    

        # 创建结果变量
        res = 1
        # 从1开始找到哈希表中第一个没有出现的正整数
        while res in hash:
            res += 1

        return res