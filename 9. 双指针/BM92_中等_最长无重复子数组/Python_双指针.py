#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr: List[int]) -> int:
        # write code here

        # 设置右指针，结果，和临时用的数组
        right = 0
        res = 0
        tmp = set()

        # 设置双循环，左指针遍历整个数组
        for i in range(len(arr)):
            # 右指针小与数组长度或右指针字符不在临时数组中间就一直向右循环
            while right < len(arr) and arr[right] not in tmp:
                # 临时数组加入新的字符
                tmp.add(arr[right])
                # 右指针向右+1
                right = right + 1
            # 更新结果，取当前值和新的数组值中的最大值
            res = max(res, right - i)
            # 临时数组清空
            tmp.remove(arr[i])
        return res
