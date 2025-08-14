#771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for i in stones:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = 0
        for key, value in d.items():
            if key in jewels:
                ans += value

        return ans
