
nums=[1,2,3,4,5,6,7,8]
n=len(nums)
for i in range (0,n-1):
    if nums[i]>nums[i+1]:
        return False
return True