## BM89_中等_合并区间

#### 题目链接 [BM89_中等_合并区间](https://www.nowcoder.com/practice/69f4e5b7ad284a478777cb2a17fb5e6a?tpId=295&tqId=691&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/r2z7HmJ/20230627102402.png)

---
## 解题思路
---
### 使用方法：遍历
---
### 题目关键信息

1. 合并所有重叠的区间
2. 合并后的区间按区间起点升序排列
---
### 解题步骤
---
1. 设置空列表用来存储最终返回结果
2. 特殊情况直接返回空列表
3. 以区间首大小来排列整个列表
4. 将排序后的第一个区间放入列表中用来比较
5. 如果排序后的区间头大于结果列表中前一个区间的区间尾，则对区间尾进行比较并存储其中较大的值
6. 将比较后的区间放入到结果列表中
7. 返回结果列表
### 最终代码
```
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
```