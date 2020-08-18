class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        Map = defaultdict(lambda:0)
        count = 0
        for i in range(len(nums)):
            Map[nums[i]] += 1
        for i in range(len(nums)):
            if(Map[nums[i]] == 1):
                return nums[i]
        