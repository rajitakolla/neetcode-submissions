class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = dict(Counter(nums))
        finalOp = sorted(result.items(), key = lambda x: x[1], reverse = True)[:k]
        resOp = list()

        for i in finalOp:
            resOp.append(i[0])

        return resOp