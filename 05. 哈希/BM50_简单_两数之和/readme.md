## BM50_简单_两数之和

#### 题目链接 [BM50_简单_两数之和)](https://www.nowcoder.com/practice/20ef0972485e41019e39543e8e895b7f?tpId=295&tqId=745&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/wM0W2hw/20230703101543.png)

---
## 解题思路
---
### 使用方法：哈希表
---
### 题目关键信息

1. 整型数组 numbers 和一个目标值 target
2. 数组中找出两个加起来等于目标值的数的下标
3. 返回的下标按升序排列，返回的数组下标从1开始算起

---
### 解题步骤
1. 创建结果变量
2. 创建哈希表
3. 遍历整型数组numbers
4. 创建临时变量，计算目标值-当前值
5. 如果哈希表中没有临时变量，给哈希表中当前值加入下标
6. 如果哈希表中有临时变量，将哈希表中临时变量的下标+1
7. 将当前值下标+1
---

### 最终代码
```
class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # write code here

        # 创建结果变量
        res = []
        # 创建哈希表,两元组分别表示值、下标
        hash = dict()

        # 在哈希表中查找target-numbers[i]
        for i in range(len(numbers)):
            temp = target - numbers[i]
            
            if temp not in hash:
                # 如果哈希表中没有临时变量，给哈希表中当前值加入下标
                hash[numbers[i]] = i            
            else:
                # 如果哈希表中有临时变量，将哈希表中临时变量的下标+1
                res.append(hash[temp]+1)
                # 将当前值下标+1
                res.append(i+1)
                break
        return res
```