#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        # write code here

        # 设置结果数组
        res = list(list())
        n = len(num)
        # 如果不够三元组则返回结果数组即空
        if n < 3:
            return res
        # 对当前数组进行排序
        num.sort()

        # 遍历
        for i in range(n - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue
            # 后续的收尾双指针
            left = i + 1
            right = n - 1
            # 设置当前数的负值为目标
            target = -num[i]
            while left < right:
                # 双指针指向的二值相加为目标，则可以与num[i]组成0
                if num[left] + num[right] == target:
                    res.append([num[i], num[left], num[right]])
                    while left + 1 < right and num[left] == num[left + 1]:
                        # 去重
                        left += 1
                    while right - 1 > left and num[right] == num[right - 1]:
                        # 去重
                        right -= 1
                    # 双指针向中间收缩
                    left += 1
                    right -= 1
                # 双指针指向的二值相加大于目标，右指针向左
                elif num[left] + num[right] > target:
                    right -= 1
                # 双指针指向的二值相加小于目标，左指针向右
                else:
                    left += 1
        return res           
            