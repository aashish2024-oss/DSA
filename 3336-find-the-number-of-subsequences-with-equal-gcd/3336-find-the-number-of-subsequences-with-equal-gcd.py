from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = max(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]  # skip x

            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue

                    # Put x into the first subsequence
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    # Put x into the second subsequence
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for g in range(1, m + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans