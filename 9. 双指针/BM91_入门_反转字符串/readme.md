## BM91_入门_反转字符串

#### 题目链接 [BM91_入门_反转字符串](https://www.nowcoder.com/practice/c3a6afee325e472386a1c4eb1ef987f3?tpId=295&tqId=1024337&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/w7tBs4b/20230627102612.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息

1. 接受一个字符串
2. 输出该字符串反转后的字符串

---
### 解题步骤
1. 设置左右指针
2. 两指针同时往中间靠 
3. 交换左右指针的字符
---

### 最终代码
```
class Solution:
    def solve(self , str: str) -> str:
        # write code here

        # 设置左右指针
        left = 0 
        right = len(str) - 1

        # 两指针同时往中间靠
        while left < right:
            res = list(str)
            temp = res[left]
            res[left] = res[right]
            # 交换左右指针的字符
            res[right] = temp
            str = ''.join(res)
            left = left + 1
            right = right - 1
        return str
```