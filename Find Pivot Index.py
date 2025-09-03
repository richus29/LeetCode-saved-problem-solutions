nums = [-1,1,2]

sumLeft = 0
sumRight = sum(nums)
for index,element in enumerate(nums):
    sumRight -= element
    if sumLeft == sumRight:
        print(index)
    sumLeft += element
