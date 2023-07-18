## BM62_入门_斐波那契数列

#### 题目链接 [BM62_入门_斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=295&tqId=23255&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/dm3Bm15/20230718162947.png)


---
## 解题思路
---
### 使用方法：动态规划
---
### 题目关键信息
1. 斐波那契数列公式为:F(n)=F(n−1)+F(n−2)
2. 初始化第1项和第2项为1
3. 求该数列第n项

---
### 解题步骤
1. 低于2项的数列，直接返回n。
2. 初始化第0项，与第1项分别为0，1.
3. 从第2项开始，逐渐按照公式累加，并更新相加数始终为下一项的前两项。
   
---

### 最终代码
```
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here

        if n < 2:
            return n
        
        res = 0
        a = 0
        b = 1

        for i in range(2, n + 1):
            res = (a + b)
            a = b
            b = res
            
        return res
```