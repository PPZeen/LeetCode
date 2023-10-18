class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ref = nums
        m = len(nums) // 2
        for i in nums:
            if target in nums[:m:]: nums = nums[:m:]
            elif target in nums[m::]: nums = nums[m::]
            else: return -1
            m = len(nums) // 2
            if m == 0: break

        return ref.index(nums[0])
    
    # def search(self, nums: List[int], target: int) -> int:
    #     i = 0
    #     m = len(nums) // 2
    #     while m - i != 1:
    #         if target in nums[:m:]:
    #             m //= 2
    #         elif target in nums[m::]:
    #             i = m
    #             m += (m//2)
    #         else : return -1
        
    #     return m if len(nums) % 2 == 0 else m+1