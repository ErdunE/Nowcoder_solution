## BM69_中等_把数字翻译成字符串

#### 题目链接 [BM69_中等_把数字翻译成字符串](https://www.nowcoder.com/practice/046a55e6cd274cffb88fc32dba695668?tpId=295&tqId=1024831&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/7SFvJCp/20230719110453.png)

---
## 解题思路
---
### 使用方法：动态规则
---
### 题目关键信息
1. 字母到数字分别为1-26映射，没有0
2. 输入的数字是字符串，故非常大，超过了long long的表示范围
3. 但凡出现11-19，21-26的就可能出现两种译码结果
4. 求总后的译码结果种类
---
### 解题步骤
1. 用辅助数组dp表示前i个数的译码方法有多少种。
2. 对于一个数，我们可以直接译码它，也可以将其与前面的1或者2组合起来译码：如果直接译码dp[i]=dp[i−1]；如果组合译码，则dp[i]=dp[i−2]。
3. 对于只有一种译码方式的，选上种dp[i−1]即可，对于满足两种译码方式（10，20不能）则是dp[i−1]+dp[i−2]
4. 依次相加，最后的dp[length]即为所求答案。
---

### 最终代码
```
class Solution:
    def solve(self , nums: str) -> int:
        # write code here

        if nums == "0":
            return 0

        if nums == "10" or nums == "20":
            return 1

        for i in range(1, len(nums)):
            if nums[i] == "0":
                if nums[i - 1] != "1" and nums[i - 1] != "2":
                    return 0

        dp = [1 for i in range(len(nums) + 1)]
        for i in range(2, len(nums) + 1):
            if (nums[i - 2] == "1" and nums[i - 1] != "0") or (nums[i - 2] == "2" and nums[i - 1] > "0" and nums[i - 1] < "7"):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[len(nums)]
```