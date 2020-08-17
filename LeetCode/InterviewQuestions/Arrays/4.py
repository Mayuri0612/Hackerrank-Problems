#check whether array contains duplicate

def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if(len(nums) == 0 or len(nums) == 1):
            return False
        '''
        for i in range(1,len(nums)):
            prev = nums[0]
            if(nums[i] != prev):
                prev = nums[i]
                return False
            elif(nums[i] == prev):
                return True
                
        '''
        if(len(nums) == len(set(nums))):
            return False
        return True