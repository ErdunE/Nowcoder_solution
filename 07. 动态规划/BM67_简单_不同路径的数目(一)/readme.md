## BM67_简单_不同路径的数目(一)

#### 题目链接 [BM67_简单_不同路径的数目(一)](https://www.nowcoder.com/practice/166eaff8439d4cd898e3ba933fbc6358?tpId=295&tqId=685&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/fFXhwZJ/20230719110314.png)

---
## 解题思路
---
### 使用方法：动态规则
---
### 题目关键信息
1. 给定一个m∗n的矩阵，要求从矩阵的左上角走到右下角的不同路径数量
2. 每次只能往下或者往右走

---
### 解题步骤
1. 用dp[i][j]表示大小为i∗j的矩阵的路径数量，下标从1开始。
2. （初始条件） 当i或者j为1的时候，代表矩阵只有一行或者一列，因此只有一种路径。
3. （转移方程） 每个格子的路径数只会来自它左边的格子数和上边的格子数，因此状态转移为dp[i][j]=dp[i−1][j]+dp[i][j−1]。
---

### 最终代码
```
class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        # write code here

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if i == 1:
                    dp[i][j] = 1
                    continue

                if j == 1:
                    dp[i][j] = 1
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]
```