class Solution:
    def moveZeroes(self, nums: list[int]) -> None:         
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[count] = nums[i]
                count += 1

        for i in range(count, len(nums)): nums[i] = 0
            
        print(nums)
    
#nums = [int(s) for s in input("Input: ").split()]
nums = [0,1,0,3,12]
#nums = [0,1,1,1,1,1,1,1,1,1,101,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,]*100000

result = Solution().moveZeroes(nums)