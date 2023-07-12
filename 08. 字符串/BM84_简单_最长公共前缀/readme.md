## BM84_简单_最长公共前缀

#### 题目链接 [BM84_简单_最长公共前缀](https://www.nowcoder.com/practice/28eb3175488f4434a4a6207f6f484f47?tpId=295&tqId=732&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/tcws96L/20230707130715.png)

---
## 解题思路
---
### 使用方法：遍历
---
### 题目关键信息

1. 给定一个字符串数组，其中有n个字符串，求所有字符串的最长公共前缀
2. 公共前缀是指所有字符串都共有的前面部分的子串，从第一个字符开始

---
### 解题步骤
1. 处理数组为空的特殊情况。
2. 因为最长公共前缀的长度不会超过任何一个字符串的长度，因此我们逐位就以第一个字符串为标杆，遍历第一个字符串的所有位置，取出字符。
3. 遍历数组中后续字符串，依次比较其他字符串中相应位置是否为刚刚取出的字符，如果是，循环继续，继续查找，如果不是或者长度不足，说明从第i位开始不同，前面的都是公共前缀。
4. 如果遍历结束都相同，最长公共前缀最多为第一个字符串。
---

### 最终代码
```
class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        # write code here
        
        #空字符串数组
        if len(strs) == 0:
            return ""
        
        #遍历第一个字符串的长度
        for i in range(len(strs[0])):
            temp = strs[0][i]
            #遍历后续的字符串
            for j in range(1, len(strs)):
                #比较每个字符串该位置是否和第一个相同                
                if i == len(strs[j]) or strs[j][i] != temp:
                    #不相同则结束
                    return strs[0][0:i]
        #后续字符串有整个字一个字符串的前缀
        return strs[0]
```