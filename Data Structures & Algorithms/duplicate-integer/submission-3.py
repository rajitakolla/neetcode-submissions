class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) < len(nums)

# Time Complexity : o(n)
# space complexity : o(n)