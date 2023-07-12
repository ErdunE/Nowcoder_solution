## BM52_中等_数组中只出现一次的两个数字

#### 题目链接 [BM52_中等_数组中只出现一次的两个数字)](https://www.nowcoder.com/practice/389fc1c3d3be4479a154f63f495abff8?tpId=295&tqId=1375231&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/9cSKM6M/20230703101922.png)

---
## 解题思路
---
### 使用方法：哈希表
---
### 题目关键信息
1. 一个整型数组
2. 两个数字只出现一次
3. 其他的数字都出现了两次


---
### 解题步骤
1. 创建哈希表
2. 创建结果变量
3. 遍历数组
4. 统计每个数字出现的个数
5. 再次遍历数组
6. 找到个数为1的两个数字
7. 排序
---

### 最终代码
```
class Solution:
    def FindNumsAppearOnce(self , nums: List[int]) -> List[int]:
        # write code here

        # 创建哈希表
        hash = dict()
        # 创建结果变量
        res = list()

        # 遍历数组
        for i in range(len(nums)):
            # 统计每个数字出现的个数
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        
        # 再次遍历数组
        for i in range(len(nums)):
            # 找到个数为1的两个数字
            if hash[nums[i]] == 1:
                res.append(nums[i])
        
        # 排序
        res.sort()

        return res
```