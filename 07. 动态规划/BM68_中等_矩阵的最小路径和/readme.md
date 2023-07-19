## BM68_中等_矩阵的最小路径和

#### 题目链接 [BM68_中等_矩阵的最小路径和](https://www.nowcoder.com/practice/7d21b6be4c6b429bb92d219341c4f8bb?tpId=295&tqId=1009012&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/Yhdt4S9/20230719110413.png)

---
## 解题思路
---
### 使用方法：动态规则
---
### 题目关键信息
1. 给定一个矩阵，从矩阵左上角到右下角，每次只能向下或者向右
2. 从左上角到右下角路径上经过的所有数字之和为路径和，求该路径和的最小值
3. 矩阵不为空，每个元素值都为非负数

---
### 解题步骤
1. 我们可以构造一个与矩阵同样大小的二维辅助数组，其中dp[i][j]表示以(i,j)位置为终点的最短路径和，则dp[0][0]=matrix[0][0]。
2. 很容易知道第一行与第一列，只能分别向右或向下，没有第二种选择，因此第一行只能由其左边的累加，第一列只能由其上面的累加。
3. 边缘状态构造好以后，遍历矩阵，补全矩阵中每个位置的dp数组值：如果当前的位置是(i，j)，上一步要么是(i−1,j)往下，要么就是(i,j−1)往右，那么取其中较小值与当前位置的值相加就是到当前位置的最小路径和，因此状态转移公式为dp[i][j]=min(dp[i−1][j],dp[i][j−1])+matrix[i][j]。
4. 最后移动到(n−1,m−1)的位置就是到右下角的最短路径和。

---

### 最终代码
```
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # write code here

        n = len(matrix) 

        m = len(matrix[0])

        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0][0] = matrix[0][0]

        for i in range(1, n):
            dp[i][0] = matrix[i][0] + dp[i - 1][0]

        for j in range(1, m):
            dp[0][j] = matrix[0][j] + dp[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = matrix[i][j] + dp[i][j - 1]
                else:
                    dp[i][j] = matrix[i][j] + dp[i - 1][j]

        return dp[n - 1][m - 1]
```