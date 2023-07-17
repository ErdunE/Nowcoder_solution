## BM99_中等_顺时针旋转矩阵

#### 题目链接 [BM99_中等_顺时针旋转矩阵](https://www.nowcoder.com/practice/2e95333fbdd4451395066957e24909cc?tpId=295&tqId=25283&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/6PNDjnh/20230712130651.png)

---
## 解题思路
---
### 使用方法：倒置翻转
---
### 题目关键信息

1. 给定一个n∗n的矩阵，返回其顺时针90度旋转后的结果

---
### 解题步骤
1. 遍历矩阵的下三角矩阵，将其与上三角矩阵对应的位置互换，其实就是数组下标交换后的互换。
2. 遍历矩阵每一行，将每一行看成一个数组使用reverse函数翻转。
---

### 最终代码
```
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here

        for i in range(n):
            for j in range(i):

                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp

        for i in range(n):
            mat[i].reverse()

        return mat
```