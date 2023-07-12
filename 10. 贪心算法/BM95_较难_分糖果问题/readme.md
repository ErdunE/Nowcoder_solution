## BM95_较难_分糖果问题

#### 题目链接 [BM95_较难_分糖果问题](https://www.nowcoder.com/practice/76039109dd0b47e994c08d8319faa352?tpId=295&tqId=1008104&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/N998s36/20230712102025.png)

---
## 解题思路
---
### 使用方法：贪心算法
---
### 题目关键信息

1. 给定一个数组，每个元素代表孩子的得分，每个孩子至少分得一个糖果
2. 相邻两个位置得分高的要比得分低的分得多，得分相同没有限制
3. 求最少总共需要多少糖果数

---
### 解题步骤
1. 使用一个辅助数组记录每个位置的孩子分到的糖果，全部初始化为1.
2. 从左到右遍历数组，如果右边元素比相邻左边元素大，意味着在递增，糖果数就是前一个加1，否则保持1不变。
3. 从右到左遍历数组，如果左边元素比相邻右边元素大， 意味着在原数组中是递减部分，如果左边在上一轮中分到的糖果数更小，则更新为右边的糖果数+1，否则保持不变。
4. 将辅助数组中的元素累加求和。
---

### 最终代码
```
class Solution:
    def candy(self , arr: List[int]) -> int:
        # write code here

        # 记录每个位置的糖果数，初始为1
        nums = [1] * len(arr)
        # 从左到右遍历
        for i in range(1, len(arr)):
            # 如果右边在递增，每次增加一个
            if arr[i] > arr[i - 1]:
                nums[i] = nums[i - 1] + 1

        # 记录总糖果数
        res = nums[len(arr) - 1]
        i = len(arr) - 2

        # 从右到左遍历
        while i >= 0:
            # 如果左边更大但是糖果数更小
            if arr[i] > arr[i + 1] and nums[i] <= nums[i + 1]:
                nums[i] = nums[i + 1] + 1
            # 累加和
            res += nums[i]
            i -= 1

        return res
```