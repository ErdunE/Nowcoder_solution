#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here

        # 创建左右指针 分别指向头尾
        left = 0
        right = len(nums) - 1

        # 左指针小与右指针就一直循环
        while left < right:
            # 设置中间指针
            mid = int((left + right) / 2)
            # 如果中间指针的数字大于其下一个数字则令右指针等于它
            if nums[mid] > nums [mid + 1]:
                right = mid
            # 反之则令左指针等于它    
            else:
                left = mid + 1

        return right
            

            
