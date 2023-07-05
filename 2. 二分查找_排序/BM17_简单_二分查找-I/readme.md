## BM17_简单_二分查找-I

#### 题目链接 [BM17_简单_二分查找-I](https://www.nowcoder.com/practice/d3df40bd23594118b57554129cadf47b?tpId=295&tqId=1499549&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/TktFbt6/20230705074008.png)

---
## 解题思路
---
### 使用方法：暴力搜索法
---
### 题目关键信息
1. 元素升序的、无重复数字的整型数组 nums 
2. 目标值 target
3. 搜索nums中是否有target
4. 有则返回对应下标，反之返回-1

---
### 解题步骤
1. 遍历数组中的数字
2. 如果当前数字等于目标值则返回其对应下标
3. 反之继续
4. 如果遍历到最后都没有，证明该数组中没有目标值，则返回-1
---

### 最终代码
```
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here


        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                continue

            i += 1

        return -1
```