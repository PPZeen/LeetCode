class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            num = nums[i]
            x = target - num
            if x in nums :
                if num != x: return [i, nums.index(x)]
                elif nums.count(x) > 1: return [i,nums.index(x,i+1)]
        return None
        
print(Solution().twoSum([1,2,3,4],4))