#Monk and rotation 

stkk = [0] * len(nums)
        for i in range(len(nums)):
            stkk[(i+k) % len(nums)] = nums[i]
            
        nums[:] = stkk
