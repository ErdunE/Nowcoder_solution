# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here

        # 设置空列表用来存储最终返回结果
        res = list()

        # 特殊情况直接返回空列表
        if len(intervals) == 0:
            return res

        # 以区间首大小来排列整个列表
        temp = sorted(intervals, key=lambda a:a.start)

        # 将排序后的第一个区间放入列表中用来比较
        res.append(temp[0])

        # 如果排序后的区间头大于结果列表中前一个区间的区间尾，则对区间尾进行比较并存储其中较大的值
        for i in range (len(temp)):
            if temp[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, temp[i].end)
            else:
                # 将比较后的区间放入到结果列表中
                res.append(temp[i])
        # 返回结果列表        
        return res
            

