## BM96_中等_主持人调度(二)

#### 题目链接 [BM96_中等_主持人调度(二)](https://www.nowcoder.com/practice/4edf6e6d01554870a12f218c94e8a299?tpId=295&tqId=1267319&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/689YJtL/20230712102125.png)

---
## 解题思路
---
### 使用方法：排序+遍历
---
### 题目关键信息
1. n个活动，有各自的区间
2. 一个主持人不能在相交的区间工作
3. 将相交的区间分成一组，最后组数即是主持人的数量
4. 数字为int型的范围，可能会出现负数

---
### 解题步骤
1. 利用辅助数组获取单独各个活动开始的时间和结束时间，然后分别开始时间和结束时间进行排序，方便后面判断是否相交。
2. 遍历n个活动，如果某个活动开始的时间大于之前活动结束的时候，当前主持人就够了，活动结束时间往后一个。
3. 若是出现之前活动结束时间晚于当前活动开始时间的，则需要增加主持人。
---

### 最终代码
```
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
```