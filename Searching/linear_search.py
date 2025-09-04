def linear_search(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

nums = [1,2,3,4,5,6,7]
target = 7

result = linear_search(nums,target)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")
