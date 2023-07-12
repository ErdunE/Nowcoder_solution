## BM53_中等_缺失的第一个正整数

#### 题目链接 [BM53_中等_缺失的第一个正整数)](https://www.nowcoder.com/practice/50ec6a5b0e4e45348544348278cdcee5?tpId=295&tqId=2188893&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/JmWpxvD/20230703102020.png)


---
## 解题思路
---
### 使用方法：哈希表
---
### 题目关键信息
1. 无重复元素的整数数组nums

---
### 解题步骤
1. 创建哈希表
2. 哈希表记录数组中出现的每个数字
3. 创建结果变量
4. 从1开始找到哈希表中第一个没有出现的正整数
---

### 最终代码
```
class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here

        # 创建哈希表
        hash = dict()

        # 哈希表记录数组中出现的每个数字
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1    

        # 创建结果变量
        res = 1
        # 从1开始找到哈希表中第一个没有出现的正整数
        while res in hash:
            res += 1

        return res
```