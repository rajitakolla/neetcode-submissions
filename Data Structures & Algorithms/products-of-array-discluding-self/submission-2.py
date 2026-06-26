class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        sizeOfArray = len(nums)
        res = [1] * sizeOfArray
        prefix = 1

        for i in range(0,sizeOfArray):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(sizeOfArray-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


        