class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i,j in enumerate(nums):
            diff = target - j
            if  i <size-1 and diff in nums[i+1:]:
                return [i,nums.index(diff,i+1)]
                break
        return [0,0]
            
        
        
        