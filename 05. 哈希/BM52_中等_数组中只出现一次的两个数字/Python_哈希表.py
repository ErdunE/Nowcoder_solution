#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self , nums: List[int]) -> List[int]:
        # write code here

        # 创建哈希表
        hash = dict()
        # 创建结果变量
        res = list()

        # 遍历数组
        for i in range(len(nums)):
            # 统计每个数字出现的个数
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        
        # 再次遍历数组
        for i in range(len(nums)):
            # 找到个数为1的两个数字
            if hash[nums[i]] == 1:
                res.append(nums[i])
        
        # 排序
        res.sort()

        return res
        
