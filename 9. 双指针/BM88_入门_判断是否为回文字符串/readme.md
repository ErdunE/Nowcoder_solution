## BM88_入门_判断是否为回文字符串

#### 题目链接 [BM88_入门_判断是否为回文字符串](https://www.nowcoder.com/practice/e297fdd8e9f543059b0b5f05f3a7f3b2?tpId=295&tqId=1089616&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/Lt1qd7H/20230627102259.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 长度为 n 的字符串
2. 回文请返回true，否则返回false
3. 回文即把相同的词汇或句子，在下文中调换位置或颠倒过来，产生首尾回环的情况，叫做回文，也叫回环。

---
### 解题步骤
---
设置双指针在字符串首，尾
依次比较是否相同
如果不同则返回False
如果相同则首指针进1，尾指针退1
直到双指针在一样位置时候，循环暂停并返回True

### 最终代码
```
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str: str) -> bool:
        # write code here
        
        # 设置双指针在字符串首，尾
        lens = len(str)
        i = 0
        j = lens - 1
        
        # 依次比较是否相同
        while i <= j:
            # 如果不同则返回False
            if str[i] != str[j]:
                return False   
            # 如果相同则首指针进1，尾指针退1             
            i = i + 1
            j = j - 1
        # 直到双指针在一样位置时候，循环暂停并返回True
        return True
```