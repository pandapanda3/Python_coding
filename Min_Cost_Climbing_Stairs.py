# Leet Code 75: 746. Min Cost Climbing Stairs
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            print(f'i is {i}, dp is {dp}')
        return dp[n]
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])