class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap = defaultdict(int)

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if hashMap[diff]:
                return [hashMap[diff], i+1]

            hashMap[numbers[i]] = i+1 
        return []

#Time complexity : o(n)
#space complexity: o(n)