nums = [2,2,2,5,1,4,2,3]
nums = sorted(set(nums), reverse=True)
greatest = max(nums)
third = 1
if len(nums) < 3:
    print(max(nums))
for i in range(len(nums)):
    if nums[i] == greatest:
        continue
    elif third == 3:
        break
    else:
        greatest = nums[i]
        third += 1
    
print(greatest)