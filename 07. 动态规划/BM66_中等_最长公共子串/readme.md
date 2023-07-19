## BM66_中等_最长公共子串

#### 题目链接 [BM66_中等_最长公共子串)](https://www.nowcoder.com/practice/f33f5adc55f444baa0e0ca87ad8a6aac?tpId=295&tqId=991150&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/PxDVB1S/20230719110222.png)

---
## 解题思路
---
### 使用方法：滑动窗口
---
### 题目关键信息
1. 查找两个字符串str1，str2中的最长的公共子串
2. 保证str1和str2的最长公共子串存在且唯一
---
### 解题步骤
1. 设置结果字符串
2. 设置左指针
3. 如果str1中的字符在str2，左指针往右移动直到没有
---

### 最终代码
```
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here

        res = ""
        left = 0
        
        for i in range(len(str1) + 1):
            if str1[left:i+1] in str2:
                res = str1[left:i+1]
            else:
                left += 1

        return res
```