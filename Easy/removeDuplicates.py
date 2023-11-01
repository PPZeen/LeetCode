class Solution:
    def removeDuplicates(self, nums: list[int]):
        check = sorted(list(set(nums)))
        nums.clear()
        
        for i in check: nums.append(i)

        return nums # return len(nums)
    

nums = [int(s) for s in input("Input: ").split()]

result = Solution().removeDuplicates(nums)

print("Output:", result)