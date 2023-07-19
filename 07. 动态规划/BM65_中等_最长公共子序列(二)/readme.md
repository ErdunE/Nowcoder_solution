## BM65_中等_最长公共子序列(二)

#### 题目链接 [BM65_中等_最长公共子序列(二)](https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=295&tqId=991075&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/M5v48fL/20230719110018.png)

---
## 解题思路
---
### 使用方法：动态规则+栈
---
### 题目关键信息
1. 找到两个字符串的最长公共子序列，子序列不要求位置在原串中连续
2. 仅存在一个最长公共子序列，不需要去重
3. 最长公共子序列为空需要返回"-1"，而不是空序列，最后要变换
---
### 解题步骤
1. 优先检查特殊情况。
2. 获取最长公共子序列的长度可以使用动态规划，我们以dp[i][j]表示在s1中以i结尾，s2中以j结尾的字符串的最长公共子序列长度。
3. 遍历两个字符串的所有位置，开始状态转移：若是i位与j位的字符相等，则该问题可以变成1+dp[i−1][j−1]，即到此处为止最长公共子序列长度由前面的结果加1。
4. 若是不相等，说明到此处为止的子串，最后一位不可能同时属于最长公共子序列，毕竟它们都不相同，因此我们考虑换成两个子问题，dp[i][j−1]或者dp[i−1][j]，我们取较大的一个就可以了。
5. 得到最长长度后，获取不需要第二个辅助数组b，直接从dp数组最后一位开始，每次比较当前位置与其左、上、左上的关系，然后将符合要求的字符加入栈中，符合要求即来自dp表格左上方的字符。
6. 最后将栈中的字符拼接即可得到最长公共子序列，注意检查子序列是否为空。
---

### 最终代码
```
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # write code here

        if len(s1) is None or len(s2) is None:
            return "-1"

        len1 = len(s1)
        len2 = len(s2)

        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i = len1
        j = len2
        s = []

        while dp[i][j] != 0:

            if dp[i][j] == dp[i - 1][j]:
                i = i - 1
            elif dp[i][j] == dp[i][j - 1]:
                j = j - 1
            elif dp[i][j] > dp[i - 1][j - 1]:
                i = i - 1
                j = j - 1
                s.append(s1[i])

        res = ""

        while len(s) != 0:
            res += s[-1]
            s.pop()
        
        if res is None or res == "":
            return "-1"
        else:
            return res
```