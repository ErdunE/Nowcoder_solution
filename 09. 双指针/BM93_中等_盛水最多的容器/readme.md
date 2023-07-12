## BM93_中等_盛水最多的容器

#### 题目链接 [BM93_中等_盛水最多的容器](https://www.nowcoder.com/practice/3d8d6a8e516e4633a2244d2934e5aa47?tpId=295&tqId=2284579&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/YZG6Rcf/20230627102752.png)
![img](https://i.ibb.co/k6WY8wL/20230627102803.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 数组height，长度为n
2. height[i]是在第i点的高度
3. 问：选2个高度与x轴组成的容器最多能容纳多少水
---
### 解题步骤
1. 特殊情况处理
2. 设置结果变量，左右指针分别指向数组首尾
3. 计算左右指针范围内的面积大小以较短指针为高，并记录面积大小
4. 依次比较面积大小并保留较大的
5. 较短指针向前移动
---

### 最终代码
```
class Solution:
    def maxArea(self , height: List[int]) -> int:
        # write code here

        # 特殊情况处理
        if len(height) < 2:
            return 0

        # 设置结果变量，左右指针分别指向数组首尾
        res = 0
        left = 0 
        right = len(height) - 1

        while left < right:
            # 计算左右指针范围内的面积大小以较短指针为高，并记录面积大小
            capacity = min(height[left], height[right]) * (right - left)
            # 依次比较面积大小并保留较大的
            res = max(res, capacity)
            # 较短指针向前移动
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return res
```