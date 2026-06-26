class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for i in nums:
            if (i-1) not in numsSet:
                length = 0
                while (i+length) in numsSet:
                    length += 1
                result = max(result, length)
        return result