#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算成功举办活动需要多少名主持人
# @param n int整型 有n个活动
# @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
# @return int整型
#
class Solution:
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int:
        # write code here

        start = list()
        end = list()
        # 分别得到活动起始时间
        for i in range(n):
            start.append(startEnd[i][0])
            end.append(startEnd[i][1])
        # 分别对开始和结束时间排序
        start.sort()
        end.sort()

        res = 0
        j = 0

        for i in range(n):
            # 新开始的节目大于上一轮结束的时间，主持人不变
            if start[i] >= end[j]:
                j += 1
            else:
                # 主持人增加
                res += 1
        
        return res
