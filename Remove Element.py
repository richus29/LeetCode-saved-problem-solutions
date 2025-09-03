nums = [0,1,2,2,3,0,4,2]
val = 2
length = len(nums)
counter = 0
i = 0

while i < len(nums):
    if nums[i] == val:
        del(nums[i])
        counter += 1
        i -= 1
    i += 1
    
    

"""for i in range(k):
    if nums[i] == val:
       
       counter += 1
nums.sort()
nums = nums[counter:]"""
print(nums)
print(length-counter)