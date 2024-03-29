## BM64_简单_最小花费爬楼梯

#### 题目链接 [BM64_简单_最小花费爬楼梯](https://www.nowcoder.com/practice/6fe0302a058a4e4a834ee44af88435c7?tpId=295&tqId=2366451&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/9bQ72LM/20230718163144.png)

---
## 解题思路
---
### 使用方法：动态规则
---
### 题目关键信息
1. 给定一个数组，其中每个元素代表该级楼梯向上爬需要支付的费用，下标从0开始
2. 一旦支付费用，可以任意选择爬一级或是二级
3. 需要求爬到顶楼，即越过数组末尾元素所需要的最小花费
4. 可以从下标为0或是1的台阶开始


---
### 解题步骤
1. 可以用一个数组记录每次爬到第i阶楼梯的最小花费，然后每增加一级台阶就转移一次状态，最终得到结果。
2. （初始状态） 因为可以直接从第0级或是第1级台阶开始，因此这两级的花费都直接为0.
3. （状态转移） 每次到一个台阶，只有两种情况，要么是它前一级台阶向上一步，要么是它前两级的台阶向上两步，因为在前面的台阶花费我们都得到了，因此每次更新最小值即可，转移方程为：dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])。
---

### 最终代码
```
class Solution:
    def minCostClimbingStairs(self , cost: List[int]) -> int:
        # write code here

        # （初始状态） 因为可以直接从第0级或是第1级台阶开始，因此这两级的花费都直接为0.
        if len(cost) <= 1:
            return 0

        # 可以用一个数组记录每次爬到第i阶楼梯的最小花费，然后每增加一级台阶就转移一次状态，最终得到结果。
        dp = [0 for i in range(len(cost) + 1)]
        # （状态转移） 每次到一个台阶，只有两种情况，要么是它前一级台阶向上一步，要么是它前两级的台阶向上两步，因为在前面的台阶花费我们都得到了，因此每次更新最小值即可，转移方程为：dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])。
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[len(cost)]
```