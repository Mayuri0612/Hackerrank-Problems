# finding index of two values that sums t given target

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for ind, val in enumerate(nums):
            temp = target - val
            if temp not in Map:
                Map[val] = ind
            else:
                res = Map[temp]
                return [res, ind]
                