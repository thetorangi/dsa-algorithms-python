def maxSubArray(nums):
    curr = nums[0]
    maxx = nums[0]
    for i in range(1,len(nums)):
      if curr < 0 :
          curr = nums[i]
      else:
          curr+=nums[i]
      if curr > maxx:
          maxx = curr
    return maxx
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f"Maximum SubArray is : {maxSubArray(nums)}")
