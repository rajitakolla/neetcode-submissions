class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        result = 0

        for val in numset:
            if (val-1) not in numset:
                temp = 1
                while (val+temp) in numset:
                    temp += 1
                result = max(result, temp)

        return result