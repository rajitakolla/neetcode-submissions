class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            diff = target - j
            if  i <len(nums)-1 and diff in nums[i+1:]:
                print(i,diff)
                return [i,nums.index(diff,i+1)]
                break
        return [0,0]
            
        
        
        