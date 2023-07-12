## BM21_简单_旋转数组的最小数字

#### 题目链接 [BM21_简单_旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=295&tqId=23269&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/LRJfGqM/20230705074440.png)

---
## 解题思路
---
### 使用方法：暴力法
---
### 题目关键信息

1. 有一个长度为 n 的非降序数组，把一个数组最开始的若干个元素“平移”到数组的末尾，变成一个旋转数组
2. 找到这个旋转数组的最小值

---
### 解题步骤
1. 创建结果变量
2. 遍历数组
3. 如果当前值小于结果变量中的值 则覆盖结果变量
4. 反之 遍历下一个值
---

### 最终代码
```
class Solution:
    def minNumberInRotateArray(self , nums: List[int]) -> int:
        # write code here

        res = nums[1]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                res = min(res, nums[i])
            else:
                continue
            i += 1
        return res
```