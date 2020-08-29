#Monk and rotation 

stk = [0] * len(nums)
        for i in range(len(nums)):
            stk[(i+k) % len(nums)] = nums[i]
            
        nums[:] = stk