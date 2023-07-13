## BM98_简单_螺旋矩阵

#### 题目链接 [BM98_简单_螺旋矩阵)](https://www.nowcoder.com/practice/7edf70f2d29c4b599693dc3aaeea1d31?tpId=295&tqId=693&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/RgZFBjV/20230712130546.png)


---
## 解题思路
---
### 使用方法：边界模拟法
---
### 题目关键信息

1. 题目给定一个n∗m的矩阵，需要将其螺旋输出

---
### 解题步骤
1. 首先排除特殊情况，即矩阵为空的情况。
2. 设置矩阵的四个边界值，开始准备螺旋遍历矩阵，遍历的截止点是左右边界或者上下边界重合。
3. 首先对最上面一排从左到右进行遍历输出，到达最右边后第一排就输出完了，上边界相应就往下一行，要判断上下边界是否相遇相交。
4. 然后输出到了右边，正好就对最右边一列从上到下输出，到底后最右边一列已经输出完了，右边界就相应往左一列，要判断左右边界是否相遇相交。
5. 然后对最下面一排从右到左进行遍历输出，到达最左边后最下一排就输出完了，下边界相应就往上一行，要判断上下边界是否相遇相交。
6. 然后输出到了左边，正好就对最左边一列从下到上输出，到顶后最左边一列已经输出完了，左边界就相应往右一列，要判断左右边界是否相遇相交。
7. 重复上述3-6步骤直到循环结束。
---

### 最终代码
```
class Solution:
    def spiralOrder(self , matrix: List[List[int]]) -> List[int]:
        # write code here

        res = list()
        n = len(matrix)
        if n == 0:
            return res

        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = n - 1

        while left <= right and up <= down:

            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1

            if up > down:
                break

            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right:
                break

            i = right
            while i >= left:
                res.append(matrix[down][i])
                i -= 1
            
            down -= 1

            if up > down:
                break

            i = down

            while i >= up:
                res.append(matrix[i][left])
                i -= 1

            left += 1

            if left > right:
                break
        
        return res
```