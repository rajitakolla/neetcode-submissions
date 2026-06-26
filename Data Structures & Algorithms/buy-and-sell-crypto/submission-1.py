class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini, maxi = 0, 1

        result = 0
        while mini < len(prices):

            if maxi< len(prices) and prices[mini] < prices[maxi]:
                result = max(result, prices[maxi]-prices[mini])
            else:
                mini = maxi

            maxi += 1

        return result
