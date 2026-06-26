class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        counterMap = defaultdict(int)

        for num in nums:
            counterMap[num] += 1

        result = list()

        for i in range(len(nums)):
            counterMap[nums[i]] -= 1

            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):

                counterMap[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue

                target = -(nums[i]+nums[j])

                if counterMap[target] > 0:
                    result.append([nums[i], nums[j], target])

            # restore values of all j which got decremented earlier
            for k in range(i+1, len(nums)):
                counterMap[nums[k]] += 1

        return result


# Time complexity : o(n^2)
# space complexity : o(n)
