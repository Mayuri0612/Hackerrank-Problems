class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums.sort()
        if(len(nums) == 0):
            return 0
        else:
            prev = nums[0]
            length = 1
            index = 1
            for i in range(1,len(nums)):
                if(nums[i] != prev):
                    length += 1
                    prev = nums[i]
                    nums[index] = nums[i]
                    index += 1
        return index
            