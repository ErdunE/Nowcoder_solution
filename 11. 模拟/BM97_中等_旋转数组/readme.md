## BM97_中等_旋转数组

#### 题目链接 [BM97_中等_旋转数组](https://www.nowcoder.com/practice/e19927a8fd5d477794dac67096862042?tpId=295&tqId=1024689&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/qpTJ06V/20230712130427.png)

---
## 解题思路
---
### 使用方法：三次翻转
---
### 题目关键信息
1. 一个长度为n的数组，将数组整体循环右移m个位置（m可能大于n）
2. 循环右移即最后m个元素放在数组最前面，前n−m个元素依次后移
3. 不能使用额外的数组空间


---
### 解题步骤
1. 因为m可能大于n，因此需要对n取余，因为每次长度为n的旋转数组相当于没有变化。
2. 第一次将整个数组翻转，得到数组的逆序，它已经满足了右移的整体出现在了左边。
3. 第二次就将左边的m个元素单独翻转，因为它虽然移到了左边，但是逆序了。
4. 第三次就将右边的n−m个元素单独翻转，因此这部分也逆序了。
---

### 最终代码
```
class Solution:
    def solve(self , n: int, m: int, a: List[int]) -> List[int]:
        # write code here

        m = m % n

        a.reverse()

        b = a[:m]
        b.reverse()

        c = a[m:]

        c.reverse()

        a[:m] = b
        a[m:] = c

        return a
```