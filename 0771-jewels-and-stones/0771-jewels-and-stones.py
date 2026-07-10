class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        s=set(jewels)
        for stone in stones:
            if stone in s:
                count+=1
        return count
        