def sort(nums):
    for i in range(0 , len(nums)):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    

nums = [10,2,5,7,8,22]
sort(nums)
print(nums)