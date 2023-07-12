## BM51_简单_数组中超过一半的数字

#### 题目链接 [BM51_简单_数组中超过一半的数字)](https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=295&tqId=23271&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/4Mm0j5Y/20230703101816.png)

---
## 解题思路
---
### 使用方法：哈希表
---
### 题目关键信息
1. 长度为 n 的数组
2. 数组中有一个数字出现的次数超过数组长度的一半
---
### 解题步骤
1. 创建哈希表
2. 遍历数组
3. 如果数字在哈希表中，对应个数加1
4. 反之没有的话 个数为1
5. 一旦在哈希表中的个数超过数组的一半 返回该数字

---

### 最终代码
```
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here

        # 创建哈希表
        hash = dict()

        # 遍历数组
        for i in range(len(numbers)):
            # 如果数字在哈希表中
            if numbers[i] in hash:
                # 对应个数加1
                hash[numbers[i]] += 1
            else:
                # 反之没有的话 个数为1
                hash[numbers[i]] = 1
            
            # 一旦在哈希表中的个数超过数组的一半 返回该数字
            if hash[numbers[i]] > (int)(len(numbers)/2):
                return numbers[i]
        
        return 0
```