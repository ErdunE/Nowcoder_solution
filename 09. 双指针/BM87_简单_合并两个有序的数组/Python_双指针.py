
#
# 
# @param A int整型一维数组 
# @param B int整型一维数组 
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        
        # 设置3个指针 分别指向数组A的最后一个 数组B的最后一个，以及数组A实际的最后一个
        i = m - 1
        j = n - 1
        p = m + n - 1

        # 比较数组A和数组B的最后一个数字，较大的放入到数组A实际最后一个
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[p] = A[i]
                i = i - 1
            else:
                A[p] = B[j]
                j = j - 1

            # 每次比较完放入较大数后将数组A最后一个数字往前进1    
            p = p - 1

        # 遍历完后如果数组B还有数字，直接遍历覆盖到数组A中
        while j >= 0:
            A[p] = B[j]
            j = j - 1
            p = p - 1
             


