## BM94_较难_接雨水问题

#### 题目链接 [BM94_较难_接雨水问题](https://www.nowcoder.com/practice/31c1aed01b394f0b8b7734de0324e00f?tpId=295&tqId=1002045&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/K5jr5nt/20230627102924.png)
![img](https://i.ibb.co/Cw6rvWr/20230627102932.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 给定一个整型数组，数组每个元素表示下图所示的每列灰色柱子高度，数值都是非负数
2. 在雨水（图中蓝色部分）不超过边界的情况下，问最多能有多少蓝色的格子
3. 数组以外的区域高度视为0

---
### 解题步骤
1. 检查数组是否为空或小于1
2. 设置结果变量，左右指针分别指向数组首尾，最大左右指针变量
3. 判断当前左右指针最大值
4. 较小一方指针开始向前移动并计算存雨量
---

### 最终代码
```
class Solution:
    def maxWater(self , arr: List[int]) -> int:
        # write code here

        # 检查数组是否为空或小于1
        if len(arr) < 1:
            return 0

        # 设置结果变量，左右指针分别指向数组首尾，最大左右指针变量
        res = 0
        left = 0
        right = len(arr) - 1
        maxL = 0
        maxR = 0

        while left < right:
            # 判断当前左右指针最大值
            maxL = max(maxL, arr[left])
            maxR = max(maxR, arr[right])
            # 较小一方指针开始向前移动并计算存雨量
            if maxL < maxR:
                res = res + maxL - arr[left]
                left = left + 1
            else:
                res = res + maxR - arr[right]
                right = right - 1

        return res
```