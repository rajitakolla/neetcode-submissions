class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in nums[i+1:]:
                j = nums[i+1:].index(diff)
                result = [i,j+i+1]
                break
        return result