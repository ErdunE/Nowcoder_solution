#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    mod = 1000000007
    def MergeSort(self, left: int, right: int, data: List[int], temp: List[int]) -> int:
         # 停止划分
        if left >= right:
            return 0
        # 取中间
        mid = int((left + right) / 2)
        # 左右划分合并
        res = self.MergeSort(left, mid, data, temp) + self.MergeSort(mid + 1, right, data, temp)
        # 防止溢出
        res %= self.mod
        i, j = left, mid + 1
        for k in range(left, right+1):
            temp[k] = data[k]
        for k in range(left, right+1):
            if i == mid + 1:
                data[k] = temp[j]
                j += 1
            elif j == right + 1 or temp[i] <= temp[j]:
                data[k] = temp[i]
                i += 1
            # 左边比右边大，答案增加
            else:
                data[k] = temp[j]
                j += 1
                # 统计逆序对
                res += mid - i + 1
        return res % self.mod
             
    def InversePairs(self , data: List[int]) -> int:
        n = len(data)
        res = [0 for i in range(n)]
        return self.MergeSort(0, n - 1, data, res)


