class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(nums.count(val)): nums.remove(val)
        return nums
    

nums = [int(s) for s in input("Input: ").split()]
val = int(input("Val: "))

result = Solution().removeElement(nums, val)

print("Output: ", result)