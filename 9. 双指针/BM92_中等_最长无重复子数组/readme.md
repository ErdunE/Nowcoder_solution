## BM92_中等_最长无重复子数组

#### 题目链接 [BM92_中等_最长无重复子数组](https://www.nowcoder.com/practice/b56799ebfd684fb394bd315e89324fb4?tpId=295&tqId=1008889&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/BqsN78C/20230627102703.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息

1. 数组arr长度为n
2. 返回arr的最长无重复元素子数组的长度

---
### 解题步骤
---

1. 设置右指针，结果，和临时用的数组
2. 设置双循环，左指针遍历整个数组
3. 右指针小与数组长度或右指针字符不在临时数组中间就一直向右循环
4. 临时数组加入新的字符
5. 右指针向右+1
6. 更新结果，取当前值和新的数组值中的最大值
7. 临时数组清空
   

### 最终代码
```
class Solution:
    def maxLength(self , arr: List[int]) -> int:
        # write code here

        # 设置右指针，结果，和临时用的数组
        right = 0
        res = 0
        tmp = set()

        # 设置双循环，左指针遍历整个数组
        for i in range(len(arr)):
            # 右指针小与数组长度或右指针字符不在临时数组中间就一直向右循环
            while right < len(arr) and arr[right] not in tmp:
                # 临时数组加入新的字符
                tmp.add(arr[right])
                # 右指针向右+1
                right = right + 1
            # 更新结果，取当前值和新的数组值中的最大值
            res = max(res, right - i)
            # 临时数组清空
            tmp.remove(arr[i])
        return res

```