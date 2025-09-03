nums = [1,1,0,1,1,1]
ans = 1
answer = 1
if len(nums) == 1 and nums[0] == 1:
    answer = 1
if len(nums) == 1 and nums[0] != 1:
    answer = 0
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] and nums[i] == 1:
        ans += 1
        if ans >= answer:
            answer = ans
    elif (nums[i] != nums[i-1] and nums[i] == 1) or (nums[i] != nums[i-1] and nums[i-1] == 1):
        if ans >= answer:
            answer = ans
        ans = 1
    else:
        ans = 1
print(answer)