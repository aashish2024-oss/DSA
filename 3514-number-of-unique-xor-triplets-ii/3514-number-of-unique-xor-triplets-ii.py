from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        values = list(set(nums))      # duplicates don't change reachable XORs
        MAX = 2048

        dp = [[False] * MAX for _ in range(4)]
        dp[0][0] = True

        for picks in range(3):
            for x in range(MAX):
                if dp[picks][x]:
                    for v in values:
                        dp[picks + 1][x ^ v] = True

        return sum(dp[3])