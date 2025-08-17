#1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        myset = sorted(set(arr))  # set in sorted order now {10,20,30,40}
        d = {}
        for ind, value in enumerate(myset):
            d[value] = ind + 1
        res = []
        for val in arr:
            res.append(d[val])

        return res