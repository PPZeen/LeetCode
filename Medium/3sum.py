def threeSum(nums):
   nums = sorted(nums)
   n = len(nums)
   ans = []
   for i in range(n-2):
      first = nums[i]
      for j in  range(i+1, n-1):
         second = nums[j]
         for k in range(j+1, n):
            third = nums[k]

            if first + second + third == 0:
               item = [first, second, third]
               duplicate = False

               for a in ans:
                  if set(a) == set(item):
                     duplicate = True
                     break

               if (not duplicate): ans.append(item)

   return ans

def threeSum2(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])

                # Move pointers and skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return ans


list_1 = [0,0,0]
list_2 = [-14,-3,11,-3,12,-1,11,13,5,6,-11,-14,-6,11,-4,-15,3,-15,9,-10,13,-10,-9,-13,-12,12,-7,12,12,3,9,5,-14,-3,9,13,11,5,3,-6,-12,-1,-5,-3,-4,-2,-10,6,-10,14,3,-11,11,10,-9,7,-1,-9,4,-12,2,-2,8,3,3,-6,-7,-1,6,12,8,9,-12,10,-8,-1,-7,-3,12,-9,-12,1,-5,6,-12,-7,-2,2,-8,-13,5,9,-7,-10,-3,11,-1,-3,-13,-10,-14,11,6,-10,6,13,4,7,-13,-6,13,12,10,-15,4,13,-7,9,-8,0,4,4,-6,12,9,-2,0]
print(threeSum2(list_2))

