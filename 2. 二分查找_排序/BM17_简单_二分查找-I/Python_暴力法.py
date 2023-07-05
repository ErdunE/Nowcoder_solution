#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here

        # 遍历数组中的数字
        for i in range(len(nums)):
            # 如果当前数字等于目标值则返回其对应下标
            if nums[i] == target:
                return i
            # 反之继续
            else:
                continue
            i += 1

        # 如果遍历到最后都没有，证明该数组中没有目标值，则返回-1
        return -1
