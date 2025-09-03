nums = [1,2,3,4]
largest = max(nums)
largest_index = nums.index(max(nums))
second_largest = max(nums[:largest_index] + nums[largest_index+1:])
if largest >= second_largest * 2:
    print(largest_index)
else:
    print(-1)
