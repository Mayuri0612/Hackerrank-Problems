# Move zeroes at end of array
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##M1
        count = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        for j in range(count, len(nums)):
            nums[j] = 0
   