#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param cost int整型一维数组 
# @return int整型
#
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