#2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                res.append(i)

        return res

