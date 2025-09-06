def trap(nums):
      l ,r = 0 , len(nums)-1
      maxL,maxR = 0,0
      total = 0
      while l < r :
          if nums[l] < nums[r]:
              if maxL < nums[l]:
                  maxL = nums[l]
              else:
                  total += maxL - nums[l]
              l+=1
          else:
              if maxR < nums[r]:
                  maxR = nums[r]
              else:
                  total += maxR - nums[r]
              r-=1
      return total
